from openai import OpenAI
import sys

client = OpenAI()


def create_file(file_path) -> str:
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="vision",
        )
        return result.id


def delete_file(file_id) -> bool:
    response = client.files.delete(file_id)
    return response.deleted


def create_conversation() -> str:
    conversation = client.conversations.create(metadata={"topic": "image-analyser-demo"})
    return conversation.id


def delete_conversation(conversation_id) -> bool:
    response = client.conversations.delete(conversation_id)
    return response.deleted


def ask_question_about_image(file_id, conversation_id, question):
    response = client.responses.create(
        model="gpt-5.2",
        conversation={"id": conversation_id},
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": question},
                {
                    "type": "input_image",
                    "file_id": file_id,
                },
            ],
        }],
    )
    return response.output_text


def ask_follow_up(conversation_id, question):
    response = client.responses.create(
        model="gpt-5.2",
        conversation={"id": conversation_id},
        input=question,
    )
    return response.output_text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: main.py <file path>")
        exit(1)

    print("Uploading file...")
    file_id = create_file(sys.argv[1])
    print("Creating conversation...")
    conversation_id = create_conversation()
    print(f"File ID: {file_id}")
    print(f"Conversation ID: {conversation_id}")

    try:
        first_question = input("Ask your first question about the image: ")
        if first_question and first_question not in {"exit", "quit", "q"}:
            response = ask_question_about_image(file_id, conversation_id, first_question)
            print(f"\n{response}\n")

            while True:
                question = input("Follow-up question (Enter to quit): ")
                if question == "exit" or question == "quit" or question == "q" or not question:
                    break
                response = ask_follow_up(conversation_id, question)
                print(f"\n{response}\n")
    finally:
        print("Removing uploaded file...")
        delete_file(file_id)
        print("Removing conversation...")
        delete_conversation(conversation_id)

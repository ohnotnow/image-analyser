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

def ask_question_about_image(file_id, question):
    response = client.responses.create(
        model="gpt-5.2",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": "what's in this image?"},
                {
                    "type": "input_image",
                    "file_id": file_id,
                },
            ],
        }],
    )
    return response.output_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: main.py <file path>")
        exit(1)
    print("Uploading file...")
    file_id = create_file(sys.argv[1])
    print(f"File ID: {file_id}")
    while True:
        question = input("What do you want to know? ")
        if question == "exit" or question == "quit" or question == "q" or not question:
            break
        response = ask_question_about_image(file_id, question)
        print(f"\n{response}\n")
    print("Removing uploaded file...")
    delete_file(file_id)


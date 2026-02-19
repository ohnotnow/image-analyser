# Image Analyser (OpenAI Vision + Files API demo)

This is a tiny demo project to show how simple it is to:

- upload an image to OpenAI using the Files API (`purpose="vision"`)
- ask questions about that image with the Responses API
- clean up by deleting the uploaded file

It is intentionally minimal and designed for learning/sharing, not production use.

## Requirements

- Python 3.14+
- `uv` for dependency management: https://docs.astral.sh/uv/
- An OpenAI API key

## Clone the repo

```bash
git clone git@github.com:ohnotnow/image-analyser.git
cd image-analyser
```

## Install dependencies with `uv`

```bash
uv sync
```

## Set your API key

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Run the demo

Pass the image path as the only argument:

```bash
uv run python main.py /path/to/your/image.jpg
```

Then type questions in the prompt. Type `exit`, `quit`, `q`, or press Enter on an empty prompt to finish.


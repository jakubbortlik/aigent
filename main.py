import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")


def main(prompt, verbose):
    client = genai.Client(api_key=api_key)

    messages = [genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)])]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(response.text)
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: You must provide a prompt.")
        sys.exit(1)
    prompt = sys.argv[1]
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True
    else:
        verbose = False
    main(prompt, verbose)

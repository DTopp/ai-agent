import os, sys
from google import genai
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)
    else:
        response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=sys.argv[1]
    )
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()

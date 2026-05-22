import asyncio
import os
import sys

from openai import AsyncOpenAI


base_url = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1/")
api_key = os.environ.get("OPENAI_API_KEY") or input(f"Enter your API key for {base_url}: ")
model = os.environ.get("OPENAI_MODEL", "openrouter/auto")

client = AsyncOpenAI(base_url=base_url, api_key=api_key)
messages = [dict(role="system", content="Just chat with the user, be friendly and helpful. Do not think. Just answer.")]

async def main() -> int:
    print(f"Using model: {model}")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        try:
            user_text = (await asyncio.to_thread(input, "you> ")).strip()
        except (EOFError, KeyboardInterrupt):
            print("Goodbye!")
            return 0

        if not user_text:
            continue

        if user_text.lower().strip() in {"/exit", "/quit"}:
            print("Goodbye!")
            return 0

        messages.append(dict(role="user", content=user_text))

        try:
            stream = await client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )
        except Exception as exc:
            print(f"error> {exc}", file=sys.stderr)
            messages.pop()
            continue

        answer_parts = []
        print("assistant> ", end="", flush=True)

        try:
            async for chunk in stream:
                if not chunk.choices:
                    continue

                token = chunk.choices[0].delta.content or ""
                if not token:
                    continue

                print(token, end="", flush=True)
                answer_parts.append(token)
        except Exception as exc:
            print(file=sys.stderr)
            print(f"error> {exc}", file=sys.stderr)
            messages.pop()
            continue

        print()
        answer = "".join(answer_parts)
        messages.append(dict(role="assistant", content=answer))


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
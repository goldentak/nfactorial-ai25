def build_openai_prompt(user_prompt: str, gemini_response: str) -> str:
    return f"""User Prompt:
{user_prompt}

Gemini Search Result:
{gemini_response}

Now analyze the information and give insights."""
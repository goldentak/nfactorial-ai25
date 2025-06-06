from agents.gemini import search_with_gemini
from agents.openai import analyze_with_openai
from prompts.analysis import build_openai_prompt

def run_analysis(user_prompt: str, gemini_key: str, openai_key: str) -> str:
    gemini_result = search_with_gemini(user_prompt, gemini_key)
    full_prompt = build_openai_prompt(user_prompt, gemini_result)
    analysis = analyze_with_openai(full_prompt, openai_key)
    return analysis

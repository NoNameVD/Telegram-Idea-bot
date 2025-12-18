from openai import AsyncOpenAI
from credits import API_KEY_AI

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY_AI,
)

async def responce_ai(requests: str) -> str:
    try:
        completion = await client.chat.completions.create(
          model="tngtech/deepseek-r1t2-chimera:free",
          messages=[
            {
              "role": "system",
              "content":"Ты помощник, который генерирует идеи проектов для пользователей. "
                        "Отвечай строго в формате: первая строка — идея, вторая строка (пустая строка), третья строка — описание (2–3 предложения)."
                        "Не более 80 слов. Без приветствий, списков и лишнего текста."
                        "Пример:"
                        "Идея: Сервис по подбору блюд из ингредиентов дома."
                        "Описание: Пользователь вводит, что есть в холодильнике, а система подбором рецептов показывает варианты блюд и шаги приготовления."
            },
            {
              "role": "user",
              "content": requests
            }
          ]
        )
        return "✅ Готово ✅\n\n" + completion.choices[0].message.content
    except Exception as e:
        return "❌ Произошли технические неполадки ❌"
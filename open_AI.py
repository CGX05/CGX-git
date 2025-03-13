# deep seek的KPI密钥
# openai.api_key='sk-134f1f8e18164b219329e0e7d5478254'

from openai import OpenAI
import time
# OPENAI
client = OpenAI(api_key="sk-134f1f8e18164b219329e0e7d5478254", base_url="https://api.deepseek.com")
# 初始化消息列表
messages=[{"role": "system", "content": "你还是个宝宝AI，你得用中文回复我"},#系统消息，用于给模型提供一些初始的指令或上下文信息。
]

while True:
    time.sleep(10)
    # 获取用户输入
    user_input=input("请输入问题，AI宝宝给您解答(输入1退出）：")
    if user_input=='1':
        break
    messages.append({"role": "user", "content":user_input})
    #调用ai_API获取回复
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False  # 指定是否以流式方式接收响应。False 表示不使用流式响应，即等待模型生成完整的回复后再一次性返回。
    )
    #AI答复
    answer=response.choices[0].message.content
    print("AI答："+answer)
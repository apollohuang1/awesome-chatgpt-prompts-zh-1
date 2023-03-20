import openai
import os
import json
import csv
import time

openai.api_key = os.getenv("OPENAI_API_KEY")


def translate_to_chinese(prompt, retries=5):
    for i in range(retries):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Please translate the following text to Simplified Chinese:\n{prompt}\n",
                temperature=0.3,
                max_tokens=4000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            return response.choices[0].text.strip()
        except openai.error.APIError as e:
            if i == retries - 1:
                raise e
            else:
                time.sleep(3)


def convert_csv_to_chinese_json():
    with open("prompts.csv", "r") as f:
        acts = []
        prompts = []
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            if i == 0:
                continue

            acts.append(row[0])

        batch_size = 15
        act_batches = [acts[i:i + batch_size]
                       for i in range(0, len(acts), batch_size)]

        translated_acts = []
        for act_batch in act_batches:
            acts_joined = "\n".join(act_batch)
            translated_acts_batch = translate_to_chinese(
                acts_joined).split("\n")
            translated_acts.extend(translated_acts_batch)

        f.seek(0)
        dialect = csv.Sniffer().sniff(f.readline(), [',', ';'])
        f.seek(0)
        reader = csv.reader(f, dialect)
        next(reader)
        for i, (translated_act, row) in enumerate(zip(translated_acts, reader)):
            prompt = {
                "act": translated_act.replace('"', ''),
                "cmd": row[0].lower().replace('"', '').replace(' ', '_'),
                "enable": True,
                "prompt": f'"{row[1]}"，请使用中文交流。'.replace('"', ''),
                "tags": [row[0].lower().replace('"', '')]
            }
            prompts.append(prompt)
    with open("prompts-zh.json", "w", encoding="utf-8") as outfile:
        json.dump(prompts, outfile, indent=4, ensure_ascii=False)
    with open("prompts-zh.csv", mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, dialect=dialect,
                            quoting=csv.QUOTE_ALL, doublequote=True)
        writer.writerow(['act', 'cmd', 'enable', 'prompt', 'tags'])
        for prompt in prompts:
            writer.writerow([prompt['act'], prompt['cmd'], prompt['enable'],
                            prompt['prompt'], ','.join(prompt['tags'])])


if __name__ == "__main__":
    convert_csv_to_chinese_json()

<h1 align="center">Welcome to awesome-chatgpt-prompts-zh 👋</h1>
<!-- ![awesome-chatgpt-prompts-zh](https://socialify.git.ci/gandli/awesome-chatgpt-prompts-zh/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Auto) -->

[![Update Prompts](https://github.com/gandli/awesome-chatgpt-prompts-zh/actions/workflows/update-prompts.yml/badge.svg)](https://github.com/gandli/awesome-chatgpt-prompts-zh/actions/workflows/update-prompts.yml)

<p>
根据 awesome-chatgpt-prompts 仓库的 prompts.csv , 翻译成中文的 prompts-zh.json。
</p>

## 🛠️ 依赖

- 😄 [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) chatGPT 提示词
- 📦 [openAI](https://openai.com/) 翻译

## 🤖️ 在 [ChatGPT](https://github.com/lencx/ChatGPT) 桌面应用程序添加 prompts

![chatgpt-cmd](https://raw.githubusercontent.com/lencx/ChatGPT/main/assets/chatgpt-cmd.gif)

## 📝 流程图

```mermaid
graph TD;
  A[检出代码] --> B[复制 prompts.csv 文件];
  B --> C[检查更改];
  C --> D{检测到更改?};
  D -- 否 --> E[退出];
  D -- 是 --> F[安装依赖];
  F --> G[翻译 prompts 到中文];
  G --> H[配置 git];
  H --> I[提交更改];
  I --> J[推送更改];
```

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

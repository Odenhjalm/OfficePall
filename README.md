# OfficePall
A GPT-powered assistant for Microsoft Office support, deployed with FastAPI + Tailwind + HTMX.

OfficePall is a GPT-powered assistant fine-tuned to provide expert support for Microsoft Office apps (Word, Excel, Outlook, etc.).  
Built with **FastAPI**, styled using **Tailwind CSS**, and enhanced with **HTMX** for snappy interactivity.

![OfficePall Demo](https://via.placeholder.com/800x200.png?text=OfficePall+UI+Preview)

---

## 🔗 Live App
> Coming soon – will be hosted on **Azure Web App**

---

## 📦 Features
- 🎯 Fast and clean user interface
- 💬 GPT-4.1 Mini fine-tuned with 4,600 Office support Q&A pairs
- 🧠 OfficeKing LoRA model with Copilot-style answers
- 🗂️ Covers Word, Excel, Outlook, Teams, OneNote, PowerPoint, and more
- 🌍 Designed for Swedish support (klar och tydlig stil)

---

## 🛠️ Tech Stack
| Layer        | Tool/Framework            |
|--------------|---------------------------|
| Backend API  | [FastAPI](https://fastapi.tiangolo.com/) |
| Frontend     | [HTMX](https://htmx.org/), [Tailwind CSS](https://tailwindcss.com/) |
| Model Host   | [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/cognitive-services/openai/) |
| DevOps       | GitHub Actions + Azure Web App (B1 plan) |

---

## 🧾 Folder Structure

```
OfficePall/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── openai_client.py
│   └── main.py
├── requirements.txt
├── startup.sh
├── azure-deploy.yml
└── README.md
```

---

## 🔒 License
See [LICENSE](LICENSE) for details.

## 👤 Author
[Robin Odenhjälm](https://linkedin.com/in/robinodenhjlm)


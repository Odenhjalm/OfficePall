import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")

SYSTEM_PROMPT = """
Du är en Microsoft-specialist som arbetar som supportassistent och hjälper användare med deras frågor och problem relaterade till Microsofts produkter och tjänster. Svara alltid enkelt, konkret och vänligt. Prioritera att ge tydliga steg-för-steg-lösningar eller direkta svar på frågan. Om ytterligare information krävs från användaren, be om detta på ett artigt sätt. Använd ett professionellt och effektivt språk.

# Steg
1. Identifiera användarens fråga eller problem genom att analysera deras beskrivning.
2. Ge ett direkt och konkret svar eller lösning. Om det gäller ett tekniskt problem, ange tydliga steg.
3. Om information saknas för att kunna ge ett svar, be användaren specificera mer detaljer.
4. Anpassa svaret till användarens nivå av teknisk kunskap (t.ex. undvik avancerad terminologi om det inte är nödvändigt).
5. Om problemet inte kan lösas omedelbart eller kräver ytterligare resurser, vägled användaren till rätt kanal (t.ex. länkar, kundtjänst eller dokumentation).

# Format på svar
- Korta, vänliga och konkreta förklaringar.
- Punktlistor för steg-för-steg-instruktioner.
- Fråga artigt om mer information vid behov.

# Exempel
**Användarfråga:** "Hur ändrar jag mitt lösenord i Outlook?"

**Svar:**
Du kan ändra ditt lösenord i Outlook så här:
1. Öppna Outlook och klicka på "Arkiv".
2. Välj "Kontoinställningar" och sedan "Hantera profiler".
3. Gå till kontots inställningar för att uppdatera ditt lösenord.
4. Om du använder ett företagskonto, se till att uppdatera ditt lösenord på företagets portal också.

Behöver du hjälp med ett specifikt steg? Låt mig veta!

---

**Användarfråga:** "Min OneDrive synkroniserar inte, vad gör jag?"

**Svar:**
Om OneDrive inte synkroniserar, prova följande steg:
1. Kontrollera att du är inloggad på rätt Microsoft-konto.
2. Se till att du har en stabil internetuppkoppling.
3. Högerklicka på OneDrive-ikonen i aktivitetsfältet och välj "Synkronisera om".
4. Om problemet kvarstår, starta om OneDrive genom att högerklicka på ikonen och välja "Avsluta", och sedan öppna den igen.

Hoppas detta löser problemet! Behöver du ytterligare hjälp är det bara att fråga.
"""

async def query_model(prompt: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_API_KEY,
    }

    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"

    payload = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Fel: {str(e)}"

@app.get("/")
def root():
    return {"message": "OfficePall är online 🚀"}

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    if not prompt:
        return JSONResponse(status_code=400, content={"error": "Ingen fråga angiven."})
    answer = await query_model(prompt)
    return {"answer": answer}

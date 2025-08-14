# 🏗️ Building Code AI Agent

An AI-powered assistant that validates **construction blueprints** against **location-specific building codes** using **Retrieval-Augmented Generation (RAG)** and a Google Cloud–hosted building code database.

---

## 🚀 Features

- **Location-Specific Code Identification** – Detects which building codes apply based on project location.
- **Violation Detection** – Checks for any/all building code violations in uploaded blueprints.
- **Detailed Compliance Feedback** – Returns results in structured JSON for easy integration with custom frontend.
- **Intelligent Topic Retrieval** – Uses RAG to fetch precise or closest-match building code data from a Vertex AI database.

---

## 🏛️ Understanding Building Codes

Building codes are regulations that define minimum standards for **design**, **construction**, and **safety** of buildings.  
For our use case at **Assembli**, we primarily reference the **International Residential Code (IRC)**.

### 📚 Code Types
- **International Residential Code (IRC)**
  - Updated every 3 years.
  - Latest versions restricted by ICC copyright.
  - 2021 and earlier versions are free online.

- **State Residential Codes**
  - Published on state government websites.
  - Often amend the IRC.
  - Examples:
    - Alabama → 2015 IRC  
    - Texas → 2012 IRC  
    - Oregon → 2021 IRC  

- **City Residential Codes**
  - Cities may amend IRC directly.
  - Examples:
    - Dallas → 2021 IRC + Dallas amendments  
    - Austin → 2024 IRC + Austin amendments  

---

## 🏗️ Project Architecture

The system is composed of **two core agents**:

### 1️⃣ Main Agent (Coordinator)
- Accepts a **construction blueprint PDF** from the user.  
- Generates a **list of relevant topics** for building code checks.  
- Sends topics to the **Sub Agent**.  
- Receives building code data and performs **violation analysis**.  
- Outputs a **structured JSON report**.

### 2️⃣ Sub Agent (RAG)
- Has RAG capabilities with access to a **Vertex AI Database** populated with building codes.  
- Queries the database for information related to received topics.  
- If exact matches aren’t found, provides **closest possible substitutes**.  
- Returns data in JSON format for the Main Agent to analyze.

---

## 📋 Usage
1. **Clone the repository**  
   ```bash
   git clone https://github.com/AbishekJayan/Building-Code-Ai-Agent.git
   cd Building-Code-Ai-Agent
   ```
2. Set up your .env file

3. Obtain the .env file with required environment variables.

4. Place it in the root directory of the project.

5. Run the project locally

```bash
adk web
```

6. **Start the conversation with text** (e.g., “Hi”) instead of immediately uploading a PDF.  

7. Wait for the AI to prompt you for a **blueprint upload**.
   
9. Upload the **construction blueprint PDF**.
    
11. Receive detailed **compliance feedback** in JSON format.

**Steps 6-11 also applies to the Deployed Version**

---

## 🔗 Links

- **Live Deployment** → [Access the AI Agent](https://building-code-agent-service-113465644709.us-central1.run.app/dev-ui/)

---

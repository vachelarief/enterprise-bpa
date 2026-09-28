# Enterprise BPA & Continuous Controls Platform - UI/UX Challenge

## 🚀 How to Run the Prototype
1. **Backend:** `cd backend`, activate venv, run `uvicorn main:app --reload` (Runs on port 8000)
2. **Frontend:** `cd frontend`, run `npm run dev` (Runs on port 3000)

---

## 📝 Key Design Decisions

**1. Information Architecture (Intent-Based Navigation)**
To avoid cognitive overload, the 8 core modules are consolidated into 6 primary navigation items based on user intent: *Action, Tracking, Configuration, Compliance, and Reporting*. Related modules are grouped (e.g., Pending Approvals and History live under "Action Center"; Workflow Catalog is accessed via a prominent primary action inside "My Requests").

**2. Dashboard Layout: Balancing Urgency & Foresight**
The dashboard serves as a "Morning Cockpit", not a comprehensive database. 
* **Immediate Urgency:** The top-left (prime real estate) is dedicated to "Pending Approvals", heavily utilizing SLA countdown timers and priority tags (P1-P3).
* **Long-term Foresight:** The top-right houses the "Expiring Controls" widget. By placing an urgent operational task next to a ticking compliance deadline, the user can manage daily bottlenecks without dropping the ball on quarterly audits.
* **Progressive Disclosure:** Widgets only show the Top 5 most urgent items. Users click "View All" to enter deep-dive workspaces.

**3. Customization Mechanism (Smart Defaults + Modular Widgets)**
To satisfy both casual and power users, the platform uses **Smart Defaults**. Upon first login, the dashboard auto-configures based on role (e.g., hiding automations if the user has no cron schedules). A "Customize Dashboard" button enables a modular layout where users can manage widgets from a catalog without complex backend configuration.

**4. Interaction Model: Context-Preserving Approvals**
Approvers suffer from context switching. To solve this in the Action Center:
* **Slide-Over Drawers:** Clicking a request opens a right-side panel containing full details, audit trails, and compliance impact. Users can approve/reject inside the drawer, close it, and immediately proceed to the next item without reloading the page.
* **Batch Actions:** Checkboxes allow bulk approvals for low-risk, routine requests, drastically reducing triage time.
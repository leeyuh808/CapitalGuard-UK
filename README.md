# **CapitalGuard UK — Ongoing Development of a Tax‑Intelligent Asset Tracker**

CapitalGuard UK is an actively evolving Django-based web application designed to give UK investors real-time insight into their investment performance and Capital Gains Tax (CGT) exposure. The platform is currently being developed to centralise trade data across multiple asset classes, automate CGT calculations, and provide users with a live view of their **£3,000 annual tax‑free allowance**.

This project is growing into a robust financial tool that blends Python-driven tax logic with SQL-backed data integrity — reflecting the standards expected in modern trading and reporting environments.

## **Why I'm Building This**
Before starting this project, I knew absolutely nothing about Capital Gains Tax.
Like… nothing.
And even now, there are still parts of it that make me stare at HMRC documentation like it’s written in ancient hieroglyphics. But that’s exactly why I’m building this: to learn by doing, to demystify something that confuses half the country, and to turn a complicated tax rule into something normal people can actually understand.
It also ties directly into the fintech space I’m aiming to grow in. Modern financial tools are expected to automate complexity, surface insights instantly, and make regulatory rules feel invisible to the user. Building CapitalGuard UK is my way of stepping into that world, taking a real tax problem, translating it into logic, and designing a system that behaves like the tools traders and investors rely on every day.

## **Current Features**

### **Real-Time Dashboard**
- Live tracking of gains, losses, and net performance  
- Dynamic updates to remaining CGT allowance  
- Instant tax liability estimates after each trade  

### **Unified Trade Ledger**
- High-precision logging of buy/sell activity  
- HMRC-aligned structure for accurate CGT calculations  
- Full audit history for compliance and transparency  

### **Automated CGT Calculations**
- Applies UK CGT rules to every trade  
- Calculates cumulative gains and allowance usage  
- Highlights when the user exceeds the tax-free threshold  

### **Multi-Page Django Architecture**
- Dashboard  
- History ledger  
- Add Trade form  
- Modular templates for scalable UI development  

## **Current Tech Stack**
______________________________________________________________

| Layer              | Tools                                 |
|--------------------|---------------------------------------|
| **Backend**        | Django, Python                        |
| **Database**       | SQLite (dev), PostgreSQL-ready        |
| **Frontend**       | Django Templates, HTML, CSS           |
| **Architecture**   | MVC pattern, modular apps             |
| **Data Integrity** | SQL-backed validation, unified ledger |
______________________________________________________________

## **Project Goal (Ongoing)**

CapitalGuard UK is being built to help traders and investors manage their tax exposure **as they trade**, not months later. Instead of discovering a large tax bill at year-end, users can see — in real time — exactly where they stand relative to their £3,000 CGT allowance.

The aim is to turn tax compliance into a continuous, automated insight rather than a stressful annual task.

## **Upcoming Features (In Progress)**

- **API integration** with trading platforms for automatic trade imports  
- **CSV import/export** for bulk trade management  
- **User authentication** for multi-user accounts  
- **Performance analytics and charts**  
- **Support for additional asset classes**  




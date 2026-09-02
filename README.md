# Sistema de Agendamento - Django + Python

### 🎯 Objetivo do Projeto
O objetivo deste projeto foi desenvolver um sistema web completo para gerenciamento de agendamentos de serviços, como barbearia, clínica ou estúdio. O problema atacado é a desorganização de agendamentos feitos via WhatsApp ou caderno, que geram conflito de horários e perda de clientes. A aplicação permite que clientes visualizem horários disponíveis e agendem, enquanto o administrador gerencia tudo pelo painel.

### ✨ Funcionalidades / Objetivos da Aplicação
- Cadastro e autenticação de usuários
- Listagem de horários disponíveis em tempo real
- Agendamento com bloqueio automático de horário já ocupado
- Cancelamento e remarcação de agendamento
- Painel administrativo para o gestor visualizar todos os agendamentos
- Validação para impedir agendamento duplicado no mesmo horário

### 🛠️ Stack / Tecnologias Utilizadas
**Back-end:** Python 3, Django 4, Django ORM
**Banco de Dados:** SQL - SQLite (dev) / PostgreSQL (prod)
**Front-end:** HTML5, CSS3, Django Templates
**Ferramentas:** Git, GitHub, Pathlib

### 🚀 Como rodar o projeto
```bash
git clone https://github.com/Paiva061/sistema-agendamento.git
cd sistema-agendamento
python -m venv venv
source venv/bin/activate # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

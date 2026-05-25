---

# 🚀 Projeto Low-Code / No-Code: Cadastro e Envio Automático de E-mails

## 📖 Sobre o Projeto

Este repositório contém a estrutura de um site de cadastro integrado com um sistema de envio automático de e-mails. O foco principal deste projeto foi explorar o potencial do desenvolvimento assistido, priorizando ferramentas de fácil acesso e configuração ágil.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Gemini Pro:** Utilizado como inteligência artificial assistente no desenvolvimento do código. Esta versão específica foi escolhida por ser disponibilizada através da instituição de ensino **UDF**.
* **Visual Studio Code (VS Code):** Ambiente de Desenvolvimento Integrado (IDE) utilizado para a estruturação do projeto.
* **Python:** Linguagem utilizada no backend para hospedar a lógica de disparo.
* **Resend API:** Plataforma de infraestrutura em nuvem responsável pelo disparo dos e-mails.

---

## ⚙️ Arquitetura e Integração

O sistema de confirmação e disparo de e-mails funciona através da API do **Resend**. A escolha por esta ferramenta se baseou nos seguintes fatores:

* **Acessibilidade:** É uma das APIs de comunicação mais fáceis de integrar atualmente no mercado.
* **Custo-Benefício:** Oferece um plano de acesso gratuito robusto para testes e pequenos projetos.
* **Funcionamento:** O Resend opera integralmente em nuvem. A conexão entre a nossa aplicação e os servidores deles é autenticada através de uma única **API Key**, que fica protegida dentro do arquivo Python.

---

## ⚠️ Desafios e Limitações do Projeto

Embora a escolha das ferramentas tenha facilitado a etapa de desenvolvimento (Low-Code/No-Code), o projeto apresentou algumas limitações em relação à infraestrutura:

* **Dependência de Configuração Externa:** Toda a gestão do serviço de e-mail é externa, exigindo configuração prévia no painel do próprio Resend antes do código funcionar.
* **Restrições de Remetente (Plano Gratuito):** O principal gargalo técnico encontrado foi a limitação da API Key no plano gratuito, que permite o vínculo e envio através de **apenas um único endereço de e-mail**. A tentativa de utilizar múltiplos remetentes exige processos adicionais de verificação de domínio e outros requisitos burocráticos dentro da conta do Resend.

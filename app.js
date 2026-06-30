// Corrigido: Linha limpa e com a URL correta
const API_URL = "https://barbearia-backend-7794.onrender.com";

async function carregarAgendamentos() {
    try {
        const response = await fetch(`${API_URL}/agendamentos`);
        const dados = await response.json();
        
        const tabela = document.getElementById("tabela-agendamentos");
        tabela.innerHTML = ""; 

        if (dados.length === 0) {
            tabela.innerHTML = `<tr><td colspan="4" class="py-4 text-center text-zinc-600">Nenhum agendamento para hoje.</td></tr>`;
            return;
        }

        dados.forEach(agendamento => {
            const dataFormatada = new Date(agendamento.data_hora).toLocaleString('pt-BR', {
                day: '2-digit', month: '2-digit', hour: '2-digit', minute:'2-digit'
            });

            tabela.innerHTML += `
                <tr class="border-b border-zinc-800 hover:bg-zinc-900/50 transition-colors text-white">
                    <td class="py-4 px-2 font-medium">${agendamento.nome_cliente}</td>
                    <td class="py-4 px-2 text-zinc-400">${agendamento.servico}</td>
                    <td class="py-4 px-2 text-zinc-400">${dataFormatada}</td>
                    <td class="py-4 px-2">
                        <span class="px-2 py-0.5 bg-zinc-800 text-zinc-300 text-xs rounded border border-zinc-700">
                            ${agendamento.status}
                        </span>
                    </td>
                </tr>
            `;
        });
    } catch (error) {
        console.error("Erro ao carregar dados:", error);
        document.getElementById("status-badge").innerText = "Backend Offline";
        document.getElementById("status-badge").className = "px-3 py-1 bg-red-950 text-red-400 border border-red-800 text-xs rounded-full";
    }
}

document.getElementById("form-agendamento").addEventListener("submit", async (e) => {
    e.preventDefault();

    const novoAgendamento = {
        nome_cliente: document.getElementById("nome").value,
        telefone: document.getElementById("telefone").value || null,
        servico: document.getElementById("servico").value,
        data_hora: document.getElementById("data_hora").value
    };

    try {
        const response = await fetch(`${API_URL}/agendamentos`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(novoAgendamento)
        });

        if (response.ok) {
            document.getElementById("form-agendamento").reset(); 
            carregarAgendamentos(); 
        } else {
            alert("Erro ao salvar o agendamento.");
        }
    } catch (error) {
        console.error("Erro ao enviar dados:", error);
    }
});

// Inicializa a listagem ao carregar a página
carregarAgendamentos();

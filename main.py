import sys
from datetime import datetime
from services.registro_consumo import RegistroConsumo
from services.generator import gerar_historico_simulado
from structures.sort import merge_sort, quick_sort
from services.busca_ordenacao import busca_sequencial, busca_binaria


def formatar_data(data):
    return data.strftime("%d/%m/%Y às %H:%M")


def main():
    registro = RegistroConsumo()

    # Dados iniciais de insumos
    insumos_estoque = [
        {"nome": "Máscaras", "quantidade": 500, "validade": "15/12/2025"},
        {"nome": "Seringas", "quantidade": 800, "validade": "20/05/2026"},
        {"nome": "Luvas", "quantidade": 600, "validade": "30/11/2025"},
        {"nome": "Reagentes", "quantidade": 200, "validade": "10/09/2025"},
        {"nome": "Álcool 70%", "quantidade": 1000, "validade": "01/03/2026"}
    ]

    # Menu inicial
    print("Deseja iniciar com um histórico simulado? (s/n): ", end="")
    if input().lower() == "s":
        historico = gerar_historico_simulado(insumos_estoque)
        for retirada in historico:
            registro.registrar_retirada(retirada['item'], retirada['quantidade'], retirada['data'])
        print("Histórico simulado carregado com sucesso!")

    while True:
        print("\n" + "=" * 40)
        print("SISTEMA DE CONTROLE DE CONSUMO")
        print("=" * 40)
        print("1. Registrar nova retirada")
        print("2. Ordenar e visualizar por quantidade")
        print("3. Ordenar e visualizar por data")
        print("4. Visualizar histórico completo (ordem cronológica)")
        print("5. Visualizar últimas retiradas (ordem inversa)")
        print("6. Buscar retiradas por insumo (busca sequencial)")
        print("7. Buscar retiradas por insumo (busca binária)")
        print("0. Sair do sistema")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- REGISTRAR NOVA RETIRADA ---")
            print("Insumos disponíveis:")
            for i, insumo in enumerate(insumos_estoque, 1):
                print(f"{i}. {insumo['nome']} - Estoque: {insumo['quantidade']}")

            try:
                escolha = int(input("Escolha o insumo (número): ")) - 1
                if 0 <= escolha < len(insumos_estoque):
                    quantidade = int(input("Quantidade retirada: "))
                    if quantidade <= insumos_estoque[escolha]['quantidade']:
                        insumos_estoque[escolha]['quantidade'] -= quantidade
                        retirada = registro.registrar_retirada(
                            insumos_estoque[escolha]['nome'],
                            quantidade,
                            datetime.now()
                        )
                        print(
                            f"✓ Retirada registrada: {quantidade} {retirada['item']} em {formatar_data(retirada['data'])}")
                    else:
                        print("❌ Quantidade indisponível em estoque!")
                else:
                    print("❌ Opção inválida!")
            except ValueError:
                print("❌ Valor inválido!")

        elif opcao == "2":
            print("\n--- RETIRADAS ORDENADAS POR QUANTIDADE ---")
            retiradas = registro.get_todas_retiradas()
            if retiradas:
                retiradas_ordenadas = merge_sort(retiradas, key=lambda x: x['quantidade'])
                for retirada in retiradas_ordenadas:
                    print(
                        f"• {retirada['quantidade']} unidades de {retirada['item']} - {formatar_data(retirada['data'])}")
            else:
                print("Nenhuma retirada registrada.")

        elif opcao == "3":
            print("\n--- RETIRADAS ORDENADAS POR DATA ---")
            retiradas = registro.get_todas_retiradas()
            if retiradas:
                retiradas_ordenadas = quick_sort(retiradas, key=lambda x: x['data'])
                for retirada in retiradas_ordenadas:
                    print(
                        f"• {formatar_data(retirada['data'])} - {retirada['quantidade']} unidades de {retirada['item']}")
            else:
                print("Nenhuma retirada registrada.")

        elif opcao == "4":
            print("\n--- HISTÓRICO COMPLETO DE RETIRADAS ---")
            retiradas = registro.get_todas_retiradas()
            if retiradas:
                for retirada in retiradas:
                    print(
                        f"• {formatar_data(retirada['data'])} - {retirada['item']}: {retirada['quantidade']} unidades")
            else:
                print("Nenhuma retirada registrada.")

        elif opcao == "5":
            print("\n--- ÚLTIMAS RETIRADAS REALIZADAS ---")
            if registro.pilha_retiradas.is_empty():
                print("Nenhuma retirada registrada.")
            else:
                # Criamos uma lista temporária para não esvaziar a pilha
                temp_list = []
                while not registro.pilha_retiradas.is_empty():
                    item = registro.pilha_retiradas.pop()
                    temp_list.append(item)
                    print(f"• {formatar_data(item['data'])} - {item['item']}: {item['quantidade']} unidades")

                # Restauramos a pilha
                for item in reversed(temp_list):
                    registro.pilha_retiradas.push(item)

        elif opcao == "6":
            print("\n--- BUSCA SEQUENCIAL POR INSUMO ---")
            nome = input("Digite o nome do insumo: ").strip()
            retiradas = registro.get_todas_retiradas()
            resultados = busca_sequencial(retiradas, nome)

            if resultados:
                print(f"\nEncontradas {len(resultados)} retiradas de {nome}:")
                for retirada in resultados:
                    print(f"• {formatar_data(retirada['data'])} - {retirada['quantidade']} unidades")
            else:
                print(f"Nenhuma retirada encontrada para {nome}.")

        elif opcao == "7":
            print("\n--- BUSCA BINÁRIA POR INSUMO ---")
            print("⚠️  Para usar busca binária, é necessário ordenar primeiro por nome do insumo.")
            print("Deseja ordenar agora? (s/n): ", end="")
            if input().lower() == "s":
                retiradas = registro.get_todas_retiradas()
                retiradas_ordenadas = merge_sort(retiradas, key=lambda x: x['item'].lower())
                nome = input("Digite o nome do insumo: ").strip()
                resultados = busca_binaria(retiradas_ordenadas, nome)

                if resultados:
                    print(f"\nEncontradas {len(resultados)} retiradas de {nome}:")
                    for retirada in resultados:
                        print(f"• {formatar_data(retirada['data'])} - {retirada['quantidade']} unidades")
                else:
                    print(f"Nenhuma retirada encontrada para {nome}.")
            else:
                print("Busca binária cancelada.")

        elif opcao == "0":
            print("Saindo do sistema...")
            sys.exit()

        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    main()
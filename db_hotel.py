import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "hotel.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


# def criar_tabela(conexao, cursor):
#     cursor.execute("CREATE TABLE IF NOT EXISTS quartos (idQuarto INTEGER NOT NULL PRIMARY KEY, localizacao VARCHAR(10), andar VARCHAR(20), tipo VARCHAR(10), arCondicionado INTEGER, valorDiaria real)")
#     cursor.execute("CREATE TABLE IF NOT EXISTS reserva (idReserva INTEGER NOT NULL PRIMARY KEY, data TEXT, responsavel VARCHAR(40), inicioPeriodo date NOT NULL, fimPeriodo date NOT NULL)")
#     cursor.execute("CREATE TABLE IF NOT EXISTS reserva_quarto (idReservaQuarto INTEGER NOT NULL PRIMARY KEY, funcionario VARCHAR(40), valorDiaria REAL NOT NULL, desconto REAL NOT NULL, valorTotalReserva REAL NOT NULL, idQuarto INTEGER, idReserva INTEGER, FOREIGN KEY (idQuarto) references quartos(idQuarto), FOREIGN KEY (idReserva) references reserva(idReserva))")
#     cursor.execute("CREATE TABLE IF NOT EXISTS hospede (idHospede INTEGER NOT NULL PRIMARY KEY, nome VARCHAR(40) NOT NULL, cpf INTEGER NOT NULL, endRua VARCHAR(40), endNumero INTEGER, endComplemento VARCHAR(20), endBairro VARCHAR(20), endCidade VARCHAR(40), endCEP INTEGER, dataNascimento TEXT, telefoneResidencial INTEGER, telefoneCelular INTEGER, identidade VARCHAR(8))")
#     cursor.execute("CREATE TABLE IF NOT EXISTS hospede_reserva (funcionario VARCHAR(40), idReserva INTEGER, idHospede INTEGER, FOREIGN KEY (idReserva) REFERENCES reserva(idReserva), FOREIGN KEY (idHospede) REFERENCES hospede(idHospede))")

#     conexao.commit()


# def inserir_quarto(
#     conexao, cursor, idQuarto, localizacao, andar, tipo, arCondicionado, valorDiaria
# ):
#     data = (idQuarto, localizacao, andar, tipo, arCondicionado, valorDiaria)
#     cursor.execute(
#         "INSERT INTO quartos (idQuarto, localizacao, andar, tipo, arCondicionado, valorDiaria) values (?,?,?,?,?,?);",
#         data,
#     )
#     conexao.commit()


# def inserir_reserva(
#     conexao, cursor, idReserva, data, responsavel, inicioPeriodo, fimPeriodo
# ):
#     data = (idReserva, data, responsavel, inicioPeriodo, fimPeriodo)
#     cursor.execute(
#         "INSERT INTO reserva (idReserva, data, responsavel, inicioPeriodo, fimPeriodo) values (?,?,?,?,?);",
#         data,
#     )
#     conexao.commit()


# def inserir_reserva_quarto(
#     conexao,
#     cursor,
#     idReservaQuarto,
#     funcionario,
#     valorDiaria,
#     desconto,
#     valorTotalReserva,
#     idQuarto,
#     idReserva,
# ):
#     data = (
#         idReservaQuarto,
#         funcionario,
#         valorDiaria,
#         desconto,
#         valorTotalReserva,
#         idQuarto,
#         idReserva,
#     )
#     cursor.execute(
#         "INSERT INTO reserva_quarto (idReservaQuarto, funcionario, valorDiaria, desconto, valorTotalReserva, idQuarto, idReserva) values (?,?,?,?,?,?,?);",
#         data,
#     )
#     conexao.commit()


# def inserir_hospede(
#     conexao,
#     cursor,
#     idHospede,
#     nome,
#     cpf,
#     endRua,
#     endNumero,
#     endComplemento,
#     endBairro,
#     endCidade,
#     endCEP,
#     dataNascimento,
#     telefone,
#     identidade,
# ):
#     data = (
#         idHospede,
#         nome,
#         cpf,
#         endRua,
#         endNumero,
#         endComplemento,
#         endBairro,
#         endCidade,
#         endCEP,
#         dataNascimento,
#         telefone,
#         identidade,
#     )
#     cursor.execute(
#         "INSERT INTO hospede (idHospede, nome, cpf, endRua, endNumero, endComplemento, endBairro, endCidade, endCEP, dataNascimento, telefone, identidade) values (?,?,?,?,?,?,?,?,?,?,?,?);",
#         data,
#     )
#     conexao.commit()


# def inserir_hospede_reserva(conexao, cursor, funcionario, idReserva, idHospede):
#     data = (funcionario, idReserva, idHospede)
#     cursor.execute(
#         "INSERT INTO hospede_reserva (funcionario, idReserva, idHospede) values (?,?,?);",
#         data,
#     )
#     conexao.commit()


# def selecionar_quarto_inferior_100(conexao, cursor, valorDiaria):
#     data = (valorDiaria,)
#     cursor.execute("SELECT * FROM quartos WHERE valorDiaria < ?", data)
#     resultado = cursor.fetchall()
#     return resultado


# criar_tabela(conexao, cursor)
# inserir_quarto(conexao, cursor, 101, "Frente", "Primeiro", "Individual", "N", 75.00)
# inserir_quarto(conexao, cursor, 102, "Fundos", "Primeiro", "Duplo",  "N", 95.00)
# inserir_quarto(conexao, cursor, 103, "Fundos", "Primeiro", "Triplo", "N", 110.00)
# inserir_quarto(conexao, cursor, 201, "Frente", "Segundo", "Individual", "S", 90.00)
# inserir_quarto(conexao, cursor, 202, "Fundos", "Segundo", "Duplo", "S", 110.00)
# inserir_quarto(conexao, cursor, 203, "Fundos", "Segundo", "Triplo", "S", 140.00)
# inserir_quarto(conexao, cursor, 301, "Frente", "Terceiro", "Individual", "S", 90.00)
# inserir_quarto(conexao, cursor, 302, "Fundos", "Terceiro", "Duplo", "S", 110.00)
# inserir_quarto(conexao, cursor, 303, "Fundos", "Terceiro", "Triplo", "S", 140.00)

# inserir_reserva(conexao, cursor, 1010, "06/11/2016", "José Abravanel", "05/01/2017", "07/01/2017")
# inserir_reserva(conexao, cursor, 1020, "25/11/2016", "Maria Antonieta", "06/01/2017", "25/01/2017")
# inserir_reserva(conexao, cursor, 1030, "01/12/2016", "Carla Cristina", "03/01/2017", "13/01/2017")
# inserir_reserva(conexao, cursor, 1040, "08/12/2016", "José Abravanel", "02/02/2017", "05/02/2017")
# inserir_reserva(conexao, cursor, 1050, "10/12/2016", "Luciano Alves", "26/12/2016", "02/01/2017")

# inserir_reserva_quarto(conexao, cursor, 10100102, "Joaquim", 95.00, 0.00, 190.00, 1040, 101)
# inserir_reserva_quarto(conexao, cursor, 10200201, "Joana", 90.00, 210.00, 1500.00, 1050, 103)
# inserir_reserva_quarto(conexao, cursor, 10300301, "Joaquim", 90.00, 0.00, 900.00, 1010, 203)
# inserir_reserva_quarto(conexao, cursor, 10400103, "Joana", 110.00, 0.00, 330.00, 1030, 302)
# inserir_reserva_quarto(conexao, cursor, 10500303, "Joana", 140.00, 80.00, 900.00, 1020, 301)

# inserir_hospede(conexao, cursor, 1, "José Abravanel", 10110210317, "Rua A", 300, "Apto 703", "Centro", "Cataguases", 'NULL', "12/01/1952", 'NULL', 37999997878, "M465321")
# inserir_hospede(conexao, cursor, 2, "Maria Antonieta", 20220130115, "Rua B", 2, "Casa Fundos", "Nova Califórnia", "Juiz de Fora", 36010450, "25/03/1980", 'NULL', 32985478965, "MG245115")
# inserir_hospede(conexao, cursor, 3, "Carla Cristina", 50548965489, "Rua C", 151, "Casa", "Sidil", "Leopoldina", 35503800, "05/05/1970", 'NULL', 37991236565, "M8854654")
# inserir_hospede(conexao, cursor, 4, "Luciano Alves", 12332154878, "Rua D", 1254, "Apto 101", "Gamboa", "Cabo Frio", 'NULL', "23/06/1979", 'NULL', 23988161654, "9879523")
# inserir_hospede(conexao, cursor, 5, "José Maria", 25456865844, "Rua E", 10, "Fundos", "São Mateus", "Juiz de Fora", 36250523, "01/08/1952", 3230328965, 'NULL', "MG240105")

# inserir_hospede_reserva(conexao, cursor, "Joaquim", 1010, 1)
# inserir_hospede_reserva(conexao, cursor, "Joana", 1020, 2)
# inserir_hospede_reserva(conexao, cursor, "Joana", 1030, 3)
# inserir_hospede_reserva(conexao, cursor, "Joaquim", 1040, 1)
# inserir_hospede_reserva(conexao, cursor, "Joana", 1050, 4)


# def mais_de_uma_hospedagem(conexao, cursor):
#     cursor.execute("""SELECT h.nome, COUNT(hr.idHospede)
#                    AS num_reservas FROM hospede h
#                    JOIN hospede_reserva hr ON h.idHospede = hr.idHospede
#                    GROUP BY hr.idHospede HAVING COUNT(hr.idHospede) > 1""")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = mais_de_uma_hospedagem(conexao, cursor)
# for mais_de_uma in resultado:
#     print(dict(mais_de_uma))


# def gastou_mais_de_100(conexao, cursor):
#     cursor.execute("""SELECT h.nome, SUM(rq.valorDiaria)
#                    AS totalGasto FROM hospede h
#                    JOIN hospede_reserva hr ON h.idHospede = hr.idHospede
#                    JOIN reserva_quarto rq ON hr.idReserva = rq.idReserva
#                    GROUP BY h.idHospede HAVING SUM(rq.valorDiaria) > 100.00""")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = gastou_mais_de_100(conexao, cursor)
# for mais_de_100 in resultado:
#     print(dict(mais_de_100))


# def hospedaram_em_janeiro_2017(conexao, cursor):
#     cursor.execute("""SELECT responsavel
#                    FROM reserva
#                    WHERE strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2))
#                    BETWEEN '2017-01-01' AND '2017-01-31'""")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = hospedaram_em_janeiro_2017(conexao, cursor)
# for jan_2017 in resultado:
#     print(dict(jan_2017))


# def informacoes_quartos(conexao, cursor):
#     cursor.execute("SELECT * FROM quartos")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = informacoes_quartos(conexao, cursor)
# for info_quartos in resultado:
#     print(dict(info_quartos))


# def informacoes_quartos_ocupados_janeiro_2017(conexao, cursor):
#     cursor.execute("""SELECT q.*
#                    FROM quartos q
#                    JOIN reserva_quarto rq ON q.idQuarto = rq.idQuarto
#                    JOIN reserva r ON rq.idReserva = r.idReserva
#                    WHERE (strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2))
#                    BETWEEN '2017-01-01' AND '2017-01-31')
#                    OR (strftime('%Y-%m-%d', substr(fimPeriodo, 7, 4) || '-' || substr(fimPeriodo, 4, 2) || '-' || substr(fimPeriodo, 1, 2))
#                    BETWEEN '2017-01-01' AND '2017-01-31')""")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = informacoes_quartos_ocupados_janeiro_2017(conexao, cursor)
# for info_quartos_ocup_jan_2017 in resultado:
#     print(dict(info_quartos_ocup_jan_2017))


# def informacoes_quartos_disponiveis_janeiro_2017(conexao, cursor):
#     cursor.execute("""SELECT q.*
#                    FROM quartos q
#                    LEFT JOIN reserva_quarto rq ON q.idQuarto = rq.idQuarto
#                    LEFT JOIN reserva r ON rq.idReserva = r.idReserva
#                    WHERE rq.idQuarto IS NULL
#                    OR ((strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2)) > '2017-01-31')
#                    OR (strftime('%Y-%m-%d', substr(fimPeriodo, 7, 4) || '-' || substr(fimPeriodo, 4, 2) || '-' || substr(fimPeriodo, 1, 2)) < '2017-01-01'))""")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = informacoes_quartos_disponiveis_janeiro_2017(conexao, cursor)
# for info_quartos_disp_jan_2017 in resultado:
#     print(dict(info_quartos_disp_jan_2017))


# def numero_quartos_ar_condicionado(conexao, cursor):
#     cursor.execute("SELECT COUNT(idQuarto) AS num_quartos FROM quartos WHERE arCondicionado = 'S'")
#     resultado = cursor.fetchone()
#     return resultado['num_quartos']


# resultado = numero_quartos_ar_condicionado(conexao, cursor)
# print(resultado)


# def quantidade_quartos_com_ar_reservados_janeiro_2017(conexao, cursor):
#     cursor.execute("""SELECT COUNT(q.idQuarto) AS num_quartos
#                    FROM quartos q
#                    JOIN reserva_quarto rq ON q.idQuarto = rq.idQuarto
#                    JOIN reserva r ON rq.idReserva = r.idReserva
#                    WHERE ((strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2)) BETWEEN '2017-01-01' AND '2017-01-31')
#                    OR (strftime('%Y-%m-%d', substr(fimPeriodo, 7, 4) || '-' || substr(fimPeriodo, 4, 2) || '-' || substr(fimPeriodo, 1, 2)) BETWEEN '2017-01-01' AND '2017-01-31'))
#                    AND arCondicionado = 'S'""")
#     resultado = cursor.fetchone()
#     return resultado['num_quartos']


# resultado = quantidade_quartos_com_ar_reservados_janeiro_2017(conexao, cursor)
# print(resultado)


# def quantidade_e_valor_diaria_quartos_sem_ar_condicionado_e_reservados_janeiro_2017(conexao, cursor):
#     cursor.execute("""SELECT COUNT(q.idQuarto) AS num_quartos, rq.valorDiaria as diaria
#                    FROM quartos q
#                    JOIN reserva_quarto rq ON q.idQuarto = rq.idQuarto
#                    JOIN reserva r ON rq.idReserva = r.idReserva
#                    WHERE ((strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2)) BETWEEN '2017-01-01' AND '2017-01-31')
#                    OR (strftime('%Y-%m-%d', substr(fimPeriodo, 7, 4) || '-' || substr(fimPeriodo, 4, 2) || '-' || substr(fimPeriodo, 1, 2)) BETWEEN '2017-01-01' AND '2017-01-31'))
#                    AND arCondicionado = 'N' """)
#     resultado = cursor.fetchall()
#     return resultado


# resultado = quantidade_e_valor_diaria_quartos_sem_ar_condicionado_e_reservados_janeiro_2017(conexao, cursor)
# for qtd_e_valorDiaria in resultado:
#     print(f"{qtd_e_valorDiaria['num_quartos']}, {qtd_e_valorDiaria['diaria']}")


# def quantidade_quartos_sem_ar_condicionado_e_reservados_fevereiro_2017(conexao, cursor):
#     cursor.execute("""SELECT COUNT (q.idQuarto) AS num_quartos
#                    FROM quartos q
#                    JOIN reserva_quarto rq ON q.idQuarto = rq.idQuarto
#                    JOIN reserva r ON rq.idReserva = r.idReserva
#                    WHERE ((strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2)) BETWEEN '2017-02-01' AND '2017-02-28')
#                    OR (strftime('%Y-%m-%d', substr(fimPeriodo, 7, 4) || '-' || substr(fimPeriodo, 4, 2) || '-' || substr(fimPeriodo, 1, 2)) BETWEEN '2017-02-01' AND '2017-02-28'))
#                    AND arCondicionado = 'N'""")
#     resultado = cursor.fetchone()
#     return resultado['num_quartos']


# resultado = quantidade_quartos_sem_ar_condicionado_e_reservados_fevereiro_2017(conexao, cursor)
# print(resultado)


# def quantidade_e_valor_diaria_quartos_com_ar_condicionado_e_reservados_fevereiro_2017(conexao, cursor):
#     cursor.execute("""SELECT COUNT(q.idQuarto) AS num_quartos, rq.valorDiaria as diaria
#                     FROM quartos q
#                     JOIN reserva_quarto rq ON q.idQuarto = rq.idQuarto
#                     JOIN reserva r ON rq.idReserva = r.idReserva
#                     WHERE ((strftime('%Y-%m-%d', substr(inicioPeriodo, 7, 4) || '-' || substr(inicioPeriodo, 4, 2) || '-' || substr(inicioPeriodo, 1, 2)) BETWEEN '2017-02-01' AND '2017-02-28')
#                     OR (strftime('%Y-%m-%d', substr(fimPeriodo, 7, 4) || '-' || substr(fimPeriodo, 4, 2) || '-' || substr(fimPeriodo, 1, 2)) BETWEEN '2017-02-01' AND '2017-02-28'))
#                     AND arCondicionado = 'S'""")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = quantidade_e_valor_diaria_quartos_com_ar_condicionado_e_reservados_fevereiro_2017(conexao, cursor)
# for qtd_e_valorDiaria in resultado:
#     print(f"{qtd_e_valorDiaria['num_quartos'], qtd_e_valorDiaria['diaria']}")


def hospedes_sem_telefone_residencial(conexao, cursor):
    cursor.execute("SELECT nome FROM hospede WHERE telefoneResidencial IS NULL")
    resultado = cursor.fetchone()
    return resultado


resultado = hospedes_sem_telefone_residencial(conexao, cursor)
print(dict(resultado))


# def hospedes_com_telefone_residencial(conexao, cursor):
#     cursor.execute("SELECT nome FROM hospede WHERE telefoneResidencial IS NOT NULL")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = hospedes_com_telefone_residencial(conexao, cursor)
# for res in resultado:
#     print(dict(res))


# def aumento_de_dez_por_cento_no_valor_diarias(conexao, cursor):
#     cursor.execute("UPDATE reserva_quarto SET valorDiaria = ROUND (valorDiaria * 1.10, 2)")
#     conexao.commit()
#     cursor.execute("SELECT idReservaQuarto, valorDiaria FROM reserva_quarto")
#     resultado = cursor.fetchall()
#     return resultado


# resultado = aumento_de_dez_por_cento_no_valor_diarias(conexao, cursor)
# for res in resultado:
#     id_reserva_quarto = res['idReservaQuarto']
#     valor_diaria = f"{res['valorDiaria']: .2f}"
#     print(dict(res))


# def corrigir_nome_funcionario_reserva_quarto(conexao, cursor):
#     cursor.execute("UPDATE reserva_quarto SET funcionario = 'Josué de Assis' WHERE idReserva = 1040")
#     conexao.commit()


# corrigir_nome_funcionario_reserva_quarto(conexao, cursor)


# def corrigir_nome_funcionario_hospede_reserva(conexao, cursor):
#     cursor.execute("UPDATE hospede_reserva SET funcionario = 'Josué de Assis' WHERE idReserva = 1040")
#     conexao.commit()


# corrigir_nome_funcionario_hospede_reserva(conexao, cursor)


# def corrigir_nome_funcionario_joana_para_maria_joana_reserva_quarto(conexao, cursor):
#     cursor.execute("UPDATE reserva_quarto SET funcionario = 'Maria Joana' WHERE funcionario = 'Joana'")
#     conexao.commit()


# corrigir_nome_funcionario_joana_para_maria_joana_reserva_quarto(conexao, cursor)


# def corrigir_nome_funcionario_joana_para_maria_joana_hospede_reserva(conexao, cursor):
#     cursor.execute("UPDATE hospede_reserva SET funcionario = 'Maria Joana' WHERE funcionario = 'Joana'")
#     conexao.commit()


# corrigir_nome_funcionario_joana_para_maria_joana_hospede_reserva(conexao, cursor)


# def corrigir_nome_hospede_tabela_hospede(conexao, cursor):
#     cursor.execute("UPDATE hospede SET nome = 'Maria Cristiana da Silva' WHERE endCidade = 'Leopoldina'")
#     conexao.commit()


# corrigir_nome_hospede_tabela_hospede(conexao, cursor)


# def corrigir_nome_hospede_tabela_reserva(conexao, cursor):
#     cursor.execute("UPDATE reserva SET responsavel = 'Maria Cristiana da Silva' WHERE idReserva = 1030")
#     conexao.commit()


# corrigir_nome_hospede_tabela_reserva(conexao, cursor)


# def corrigir_rua_hospede_leopoldina(conexao, cursor):
#     cursor.execute("UPDATE hospede SET endRua = 'Rua Álvares de Azevedo' WHERE endCidade = 'Leopoldina'")
#     conexao.commit()


# corrigir_rua_hospede_leopoldina(conexao, cursor)


# def excluir_hospede_com_telefone_residencial(conexao, cursor):
#     cursor.execute("DELETE FROM hospede WHERE telefoneResidencial IS NOT NULL")
#     conexao.commit()


# excluir_hospede_com_telefone_residencial(conexao, cursor)

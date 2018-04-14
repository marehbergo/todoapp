from flask import Flask, jsonify

app = Flask('todoapp')
tarefas = [{'id': 1, 'titulo': 'tarefa 1',
            'descricao': 'tarefa de numero 1', 'estado': False}]

@app.route('/tarefas')
def listar():
    return jsonify(tarefas)

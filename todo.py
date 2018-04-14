from flask import Flask, jsonify

app = Flask('todoapp')
tarefas = []

@app.route('/tarefas')
def listar():
    return jsonify(tarefas)

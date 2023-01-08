import 'package:flutter/material.dart';
import 'todo.dart';

class ToDoItem extends StatelessWidget {
  final ToDo todo;
  final onToDoChanged;
  final onDeleteItem;

  const ToDoItem({
    Key? key,
    required this.todo,
    required this.onToDoChanged,
    required this.onDeleteItem,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(bottom: 20),
        child: Row(
            children : [
              Expanded(
                flex: 5,
                child: Text(
                  todo.todoText,
                  style: TextStyle(
                  decoration: todo.isDone ? TextDecoration.lineThrough : null,
                  fontSize: 20)
                ),
              ),
              Expanded(
                  child:
                  IconButton(
                    onPressed: (){
                      onToDoChanged(todo);
                    },
                    icon: Icon(
                      todo.isDone ? Icons.check_box : Icons.check_box_outline_blank,
                    ),
                    color: Colors.lightGreen,
                  )
              ),
              Expanded(child: IconButton(
                onPressed: (){
                  onDeleteItem(todo.id);
                },
                icon: Icon(Icons.delete),
                  color: Colors.black
              )
              )
        ]
        )
    );
  }
}
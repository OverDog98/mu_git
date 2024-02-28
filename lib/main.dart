import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xff1b1f23),
          title: Row(
            children: [
              Expanded(
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    IconButtonWithDropdown(
                      icon: Icons.face, // 이모티콘 변경 필요
                      text: '버튼 텍스트 1', // 텍스트 변경 필요
                    ),
                    IconButtonWithDropdown(
                      icon: Icons.face, // 이모티콘 변경 필요
                      text: '버튼 텍스트 2', // 텍스트 변경 필요
                    ),
                    IconButton(
                      icon: Icon(Icons.face), // 이모티콘 변경 필요
                      onPressed: () {},
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class IconButtonWithDropdown extends StatefulWidget {
  final IconData icon;
  final String text;

  IconButtonWithDropdown({required this.icon, required this.text});

  @override
  _IconButtonWithDropdownState createState() => _IconButtonWithDropdownState();
}

class _IconButtonWithDropdownState extends State<IconButtonWithDropdown> {
  bool _showDropdown = false;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        GestureDetector(
          onTap: () {
            setState(() {
              _showDropdown = !_showDropdown;
            });
          },
          child: Row(
            children: [
              Icon(widget.icon),
              Text(widget.text),
              Icon(_showDropdown ? Icons.arrow_drop_up : Icons.arrow_drop_down),
            ],
          ),
        ),
        if (_showDropdown)
          Container(
            width: double.infinity,
            color: Colors.white,
            child: Text(
              '드롭다운 메뉴', // 드롭다운 메뉴 내용 변경 필요
              style: TextStyle(color: Colors.black),
            ),
          ),
      ],
    );
  }
}

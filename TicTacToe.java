

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class TicTacToe extends JFrame implements ActionListener {
    private static final long serialVersionUID = 1L;
    private static JButton[] buttons = new JButton[9];
    private int[] board = new int[9];
    private int currentPlayer = 1;
    private int moves = 0;
    

    public TicTacToe() {
        super("Tic Tac Toe");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(3, 3));
        for (int i = 0; i < 9; i++) {
            buttons[i] = new JButton();
            buttons[i].setFont(new Font("Arial", Font.PLAIN, 48));
            buttons[i].addActionListener(this);
            add(buttons[i]);
        }
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < 9; i++) {
            if (e.getSource() == buttons[i]) {
                if (board[i] == 0) {
                    board[i] = currentPlayer;
                    buttons[i].setText(currentPlayer == 1 ? "X" : "O");
                    currentPlayer ^= 3;
                    moves++;
                }
            }
        }
    }

    

  


   

    public boolean isTie() {
        return moves == 9;
    }

    public static void main(String[] args) {
        new TicTacToe();
    }

    

    
}
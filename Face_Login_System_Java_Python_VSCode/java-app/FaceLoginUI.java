import javax.swing.*;
import java.io.*;

public class FaceLoginUI {
    private static final String PYTHON_EXE = "C:\\Users\\MOURYA\\AppData\\Local\\Programs\\Python\\Python39\\python.exe";
    private static final String REGISTER_SCRIPT = "../python-face-api/register_face.py";
    private static final String RECOGNIZE_SCRIPT = "../python-face-api/recognize_face.py";

    public static void main(String[] args) {
        JFrame frame = new JFrame("Face Login System");
        JButton registerBtn = new JButton("Register Face");
        JButton loginBtn = new JButton("Login with Face");

        registerBtn.setBounds(100, 100, 200, 40);
        loginBtn.setBounds(100, 160, 200, 40);

        frame.add(registerBtn);
        frame.add(loginBtn);

        registerBtn.addActionListener(e -> runPythonScript(PYTHON_EXE, REGISTER_SCRIPT));
        loginBtn.addActionListener(e -> runPythonScript(PYTHON_EXE, RECOGNIZE_SCRIPT));

        frame.setSize(400, 300);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void runPythonScript(String pythonExe, String scriptPath) {
        try {
            ProcessBuilder pb = new ProcessBuilder(pythonExe, scriptPath);
            pb.redirectErrorStream(true);
            Process p = pb.start();

            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode = p.waitFor();
            System.out.println("Process exited with code: " + exitCode);
        } catch (IOException | InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}

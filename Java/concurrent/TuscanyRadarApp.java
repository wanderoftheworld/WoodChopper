import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.URL;
import javax.imageio.ImageIO;
import javax.swing.*;

public class TuscanyRadarApp extends JFrame {

    private JLabel imageLabel;
    private final String radarImageUrl = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png";

    public TuscanyRadarApp() throws IOException {
        super("Tuscany Live Radar");
        imageLabel = new JLabel();
        updateImage();
        
        add(imageLabel, BorderLayout.CENTER);
        pack();
        setVisible(true);
    }

    private void updateImage() throws IOException {
        URL url = new URL(radarImageUrl);
        BufferedImage image = ImageIO.read(url);
        ImageIcon icon = new ImageIcon(image);
        imageLabel.setIcon(icon);
    }

    public static void main(String[] args) throws IOException {
        new TuscanyRadarApp();
    }
}

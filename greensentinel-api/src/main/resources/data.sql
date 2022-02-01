DROP TABLE device IF EXISTS;

CREATE TABLE device (
      id INT AUTO_INCREMENT PRIMARY KEY,
      status VARCHAR(50),
      date DATE DEFAULT CURRENT_DATE ,
      temperature NUMBER,
      humidity NUMBER,
      luminosity NUMBER
);

INSERT INTO device (id, status, date, temperature, humidity, luminosity) VALUES
    (1, 'ON', CURRENT_TIMESTAMP, 29, 65, 800),
    (2, 'ON', CURRENT_TIMESTAMP, 25, 74, 850),
    (3, 'ON', CURRENT_TIMESTAMP, 24, 66, 900);

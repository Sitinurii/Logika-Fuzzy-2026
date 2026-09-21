CREATE DATABASE logika_fuzzy;

-- Setelah database dibuat, masuk ke database logika_fuzzy
-- \c logika_fuzzy


CREATE TABLE domain_bayi (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO domain_bayi (b_bawah, b_atas, fungsi) VALUES
(0, 2, '1'),
(2, 5, 'trapesium_down_bayi'),
(5, 150, '0');


CREATE TABLE domain_anak (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO domain_anak (b_bawah, b_atas, fungsi) VALUES
(0, 2, '0'),
(2, 4, 'trapesium_up_anak'),
(4, 10, '1'),
(10, 12, 'trapesium_down_anak'),
(12, 150, '0');


CREATE TABLE domain_remaja (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO domain_remaja (b_bawah, b_atas, fungsi) VALUES
(0, 10, '0'),
(10, 12, 'trapesium_up_remaja'),
(12, 16, '1'),
(16, 18, 'trapesium_down_remaja'),
(18, 150, '0');


CREATE TABLE domain_pemuda (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO domain_pemuda (b_bawah, b_atas, fungsi) VALUES
(0, 16, '0'),
(16, 18, 'trapesium_up_pemuda'),
(18, 22, '1'),
(22, 25, 'trapesium_down_pemuda'),
(25, 150, '0');


CREATE TABLE domain_dewasa (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO domain_dewasa (b_bawah, b_atas, fungsi) VALUES
(0, 22, '0'),
(22, 30, 'trapesium_up_dewasa'),
(30, 55, '1'),
(55, 65, 'trapesium_down_dewasa'),
(65, 150, '0');


CREATE TABLE domain_lansia (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO domain_lansia (b_bawah, b_atas, fungsi) VALUES
(0, 60, '0'),
(60, 65, 'trapesium_up_lansia'),
(65, 150, '1');
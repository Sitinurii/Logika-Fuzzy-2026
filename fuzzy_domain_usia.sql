CREATE DATABASE fuzzy_db;

\c fuzzy_db

-- 1. Bayi / Anak Usia Dini
CREATE TABLE tb_domain_usia_bayi (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO tb_domain_usia_bayi (b_bawah, b_atas, fungsi) VALUES
(0, 1, 'trapesium_up_bayi'),
(1, 4, '1'),
(4, 5, 'trapesium_down_bayi'),
(5, 150, '0');

-- 2. Anak-anak
CREATE TABLE tb_domain_usia_anak (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO tb_domain_usia_anak (b_bawah, b_atas, fungsi) VALUES
(0, 6, '0'),
(6, 7, 'trapesium_up_anak'),
(7, 10, '1'),
(10, 11, 'trapesium_down_anak'),
(11, 150, '0');

-- 3. Remaja
CREATE TABLE tb_domain_usia_remaja (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO tb_domain_usia_remaja (b_bawah, b_atas, fungsi) VALUES
(0, 10, '0'),
(10, 12, 'trapesium_up_remaja'),
(12, 17, '1'),
(17, 19, 'trapesium_down_remaja'),
(19, 150, '0');

-- 4. Pemuda
CREATE TABLE tb_domain_usia_pemuda (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO tb_domain_usia_pemuda (b_bawah, b_atas, fungsi) VALUES
(0, 15, '0'),
(15, 17, 'trapesium_up_pemuda'),
(17, 22, '1'),
(22, 24, 'trapesium_down_pemuda'),
(24, 150, '0');

-- 5. Dewasa
CREATE TABLE tb_domain_usia_dewasa (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO tb_domain_usia_dewasa (b_bawah, b_atas, fungsi) VALUES
(0, 20, '0'),
(20, 30, 'trapesium_up_dewasa'),
(30, 55, '1'),
(55, 65, 'trapesium_down_dewasa'),
(65, 150, '0');

-- 6. Lansia
CREATE TABLE tb_domain_usia_lansia (
    id SERIAL PRIMARY KEY,
    b_bawah INT NOT NULL,
    b_atas INT NOT NULL,
    fungsi VARCHAR(100) NOT NULL
);

INSERT INTO tb_domain_usia_lansia (b_bawah, b_atas, fungsi) VALUES
(0, 65, '0'),
(65, 68, 'trapesium_up_lansia'),
(68, 77, '1'),
(77, 80, 'trapesium_down_lansia'),
(80, 150, '0');
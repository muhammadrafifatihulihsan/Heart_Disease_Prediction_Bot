# README

## Deskripsi Umum

Proyek ini merupakan implementasi model K-Nearest Neighbor (KNN) yang dijalankan secara lokal dan diintegrasikan ke dalam bot Telegram. Sistem ini dirancang sebagai sarana pembelajaran untuk memahami alur kerja machine learning, mulai dari pengolahan data, pelatihan model, evaluasi, hingga penggunaan model dalam aplikasi nyata.

PENTING: Sistem ini hanya menghasilkan prediksi berbasis data dan algoritma, bukan diagnosis medis. Hasil prediksi tidak dapat dijadikan acuan tunggal dan pengguna tetap disarankan untuk berkonsultasi dengan dokter atau tenaga medis profesional.

## K-Nearest Neighbor (KNN)

KNN adalah algoritma supervised learning yang bekerja dengan membandingkan data baru terhadap sejumlah data terdekat pada data latih berdasarkan jarak tertentu. Kelas atau nilai prediksi ditentukan dari mayoritas tetangga terdekat tersebut.

## Pemisahan Fitur dan Label

Pada tahap ini, dataset dipisahkan menjadi dua bagian utama, yaitu fitur sebagai variabel input dan label sebagai target output yang akan diprediksi oleh model.

## Encoding Label (Presence / Absence)

Label kategorikal diubah ke dalam bentuk numerik agar dapat diproses oleh algoritma KNN. Proses ini memastikan model dapat memahami perbedaan kelas secara matematis.

## Feature Scaling

Fitur dinormalisasi agar seluruh variabel berada pada skala yang sebanding. Langkah ini penting karena KNN sangat bergantung pada perhitungan jarak antar data.

## Split Data Train dan Test

Dataset dibagi menjadi data latih dan data uji. Data latih digunakan untuk membangun model, sedangkan data uji digunakan untuk mengukur kemampuan generalisasi model.

## Training Model KNN

Model KNN dilatih menggunakan data latih dengan parameter tertentu seperti jumlah tetangga terdekat. Pada tahap ini, model mulai mempelajari pola dari data.

## Evaluasi Model

Performa model dievaluasi menggunakan data uji untuk mengetahui tingkat akurasi dan kemampuan prediksi. Evaluasi ini digunakan sebagai dasar penilaian kualitas model.

## Testing atau Prediksi Data Baru

Model yang telah dilatih digunakan untuk memprediksi data baru sebagai simulasi penggunaan oleh pengguna. Hasil prediksi ditampilkan sebagai output sistem.

## Penyimpanan Model

Model disimpan ke dalam file agar dapat digunakan kembali tanpa perlu melakukan pelatihan ulang setiap kali aplikasi dijalankan atau ada pengguna baru.

## Integrasi dengan Bot Telegram

Model yang telah disimpan dimuat kembali saat bot dijalankan. Bot Telegram menerima input dari pengguna, memprosesnya menggunakan model KNN, dan mengembalikan hasil prediksi secara otomatis.

## Catatan Penting

- Sistem ini bersifat prediktif dan edukatif
- Hasil prediksi tidak bersifat mutlak
- Tetap diperlukan konsultasi dengan dokter atau tenaga ahli terkait

## Tujuan Pembelajaran

- Memahami alur kerja machine learning secara menyeluruh
- Mengimplementasikan model KNN secara lokal
- Mengintegrasikan model ke dalam aplikasi bot Telegram
- Meningkatkan pemahaman tentang penerapan AI secara praktis

- rafiieee

import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('divorece_model.sav', 'rb'))

st.title('Prediksi Perceraian')
st.subheader('- Isi tanggapan dengan skala 5 poin :')
st.text('0=Tidak pernah, 1=Jarang, 2=Rata-rata, 3=Sering, 4=Selalu.')

Q1 = st.text_input('Jika salah satu dari kami meminta maaf saat diskusi kami memburuk, diskusi berakhir.')

Q2 = st.text_input('Saya tahu kita bisa mengabaikan perbedaan kita, bahkan jika terkadang keadaan menjadi sulit.')

Q3 = st.text_input('Ketika kami membutuhkannya, kami dapat berdiskusi dengan pasangan saya dari awal dan memperbaikinya.')

Q4 = st.text_input('Ketika saya berdiskusi dengan pasangan saya, menghubungi dia pada akhirnya akan berhasil.')

Q5 = st.text_input('Waktu yang saya habiskan bersama istri saya spesial bagi kami.')

Q6 = st.text_input('Kami tidak punya waktu di rumah sebagai mitra.')

Q7 = st.text_input('Kami seperti dua orang asing yang berbagi lingkungan yang sama di rumah daripada keluarga.')

Q8 = st.text_input('Saya menikmati liburan kami dengan istri saya.')

Q9 = st.text_input('Saya senang bepergian dengan istri saya.')

Q10 = st.text_input('Sebagian besar tujuan kita sama dengan pasangan saya.')

Q11 = st.text_input('Saya pikir suatu hari nanti, ketika saya melihat ke belakang, saya melihat bahwa pasangan saya dan saya telah rukun satu sama lain.')

Q12 = st.text_input('Pasangan saya dan saya memiliki nilai yang sama dalam hal kebebasan pribadi.')

Q13 = st.text_input('Pasangan saya dan saya memiliki selera hiburan yang sama.')

Q14 = st.text_input('Sebagian besar tujuan kita untuk orang (anak-anak, teman, dll.) Adalah sama.')

Q15 = st.text_input('Impian kami dengan pasangan saya serupa dan harmonis.')

Q16 = st.text_input('Kami cocok dengan pasangan saya tentang apa itu cinta.')

Q17 = st.text_input('Kami berbagi pandangan yang sama tentang menjadi bahagia dalam hidup kami dengan pasangan saya.')

Q18 = st.text_input('Pasangan saya dan saya memiliki gagasan yang sama tentang bagaimana pernikahan seharusnya.')

Q19 = st.text_input('Pasangan saya dan saya memiliki gagasan yang sama tentang bagaimana seharusnya peran dalam pernikahan.')

Q20 = st.text_input('Pasangan saya dan saya memiliki nilai kepercayaan yang sama.')

Q21 = st.text_input('Saya tahu persis apa yang disukai istri saya.')

Q22 = st.text_input('Saya tahu bagaimana pasangan saya ingin dirawat ketika dia sakit.')

Q23 = st.text_input('Saya tahu makanan favorit pasangan saya.')

Q24 = st.text_input('Saya dapat memberi tahu Anda jenis stres apa yang dihadapi pasangan saya dalam hidupnya.')

Q25 = st.text_input('Saya memiliki pengetahuan tentang dunia batin pasangan saya.')

Q26 = st.text_input('Saya tahu kecemasan dasar pasangan saya.')

Q27 = st.text_input('Saya tahu apa sumber stres pasangan saya saat ini.')

Q28 = st.text_input('Saya tahu harapan dan keinginan pasangan saya.')

Q29 = st.text_input('Saya sangat mengenal pasangan saya.')

Q30 = st.text_input('Saya mengenal teman-teman pasangan saya dan hubungan sosial mereka.')

Q31 = st.text_input('Saya merasa agresif ketika saya berdebat dengan pasangan saya.')

Q32 = st.text_input('Saat berdiskusi dengan pasangan saya, saya biasanya menggunakan ekspresi seperti kamu selalu atau kamu tidak pernah.')

Q33 = st.text_input('Saya dapat menggunakan pernyataan negatif tentang kepribadian pasangan saya selama diskusi kami.')

Q34 = st.text_input('Saya dapat menggunakan ekspresi ofensif selama diskusi kami.')

Q35 = st.text_input('Saya dapat menghina pasangan saya selama diskusi kami.')

Q36 = st.text_input('Saya bisa mempermalukan saat kita berdiskusi.')

Q37 = st.text_input('Diskusi saya dengan pasangan saya tidak tenang.')

Q38 = st.text_input('Saya benci cara pasangan saya membuka topik.')

Q39 = st.text_input('Diskusi kami sering terjadi secara tiba-tiba.')

Q40 = st.text_input('Kami baru saja memulai diskusi sebelum saya tahu apa yang terjadi.')

Q41 = st.text_input('Ketika saya berbicara dengan pasangan saya tentang sesuatu, ketenangan saya tiba-tiba hilang.')

Q42 = st.text_input('Ketika saya berdebat dengan pasangan saya, saya hanya keluar dan tidak mengatakan sepatah kata pun.')

Q43 = st.text_input('Saya kebanyakan diam untuk sedikit menenangkan lingkungan.')

Q44 = st.text_input('Kadang-kadang saya pikir itu baik bagi saya untuk meninggalkan rumah untuk sementara waktu.')

Q45 = st.text_input('Saya lebih suka diam daripada berdiskusi dengan pasangan saya.')

Q46 = st.text_input('Bahkan jika saya benar dalam diskusi, saya tetap diam untuk menyakiti pasangan saya.')

Q47 = st.text_input('Saat saya berdiskusi dengan pasangan saya, saya diam saja karena takut tidak bisa mengendalikan amarah saya.')

Q48 = st.text_input('Saya merasa benar dalam diskusi kami.')

Q49 = st.text_input('Saya tidak ada hubungannya dengan apa yang dituduhkan kepada saya.')

Q50 = st.text_input('Saya sebenarnya bukan orang yang bersalah atas apa yang dituduhkan kepada saya.')

Q51 = st.text_input('Saya bukan orang yang salah tentang masalah di rumah.')

Q52 = st.text_input('Saya tidak akan ragu untuk memberi tahu pasangan saya tentang kekurangannya.')

Q53 = st.text_input('Ketika saya berdiskusi, saya mengingatkan pasangan saya tentang kekurangannya.')

Q54 = st.text_input('Saya tidak takut untuk memberi tahu pasangan saya tentang ketidakmampuannya.')

prediksi_percerraian = ''

if st.button('Prediksi Perceraian'):
    prediksi_percerraian = model.predict([[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40, Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50, Q51, Q52, Q53, Q54]])
    
    if (prediksi_percerraian[0]==1):
        prediksi_percerraian = 'Pasangan Melakukan Perceraian'
    else:
        prediksi_percerraian = ' Pasangan Tidak Melakukan Perceraian'
        
st.success(prediksi_percerraian)
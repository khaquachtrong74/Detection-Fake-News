# import pandas as pd
# import string
# thanhnien = pd.read_csv('data_thanhnien5.csv')
# thanhnien = thanhnien[thanhnien['Date'].str.contains('2024-07-26|2024-07-27')]
# thanhnien = thanhnien[thanhnien['Content'].str.len() > 20]
# thanhnien.to_csv('data_thanhnien5.csv', index=False)

# soha = pd.read_csv('Data_soha5.csv')
# soha = soha[soha['Date'].str.contains('2024-07-25')]
# soha = soha[soha['Content'].str.len() > 10]
# soha.to_csv('Data_soha5.csv', index=False)


# tuoitre = pd.read_csv('Data_tuoitre5.csv')
# tuoitre = tuoitre[tuoitre['Date'].str.contains('2024-07-25')]
# tuoitre = tuoitre[tuoitre['Content'].str.len() > 10]
# s1 = "Chia sẻ về xu hướng nghề nghiệp mới trong những năm gần đây, giúp các bạn trẻ có cái nhìn toàn cảnh để định hướng bản thân trong tương lai"
# s2 = "Chọn lý do vi phạm : Xúc phạm, gây hại người khác Lạc đề Vi phạm pháp luật Vi phạm đạo đức, thuần phong mỹ tục Tố cáo sai sự thật Vi phạm bản quyền Để lộ thông tin cá nhân Spam, rác Lý do khácÝ kiến :"
# tuoitre=tuoitre[~tuoitre["Content"].str.contains(s2, na=False)]

# tuoitre.to_csv('Data_tuoitre5.csv', index=False)
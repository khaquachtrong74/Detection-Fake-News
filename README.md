# Detection Fake News (Vietnamese)

Dự án xây dựng hệ thống phát hiện tin giả tiếng Việt sử dụng các kỹ thuật Học máy (Machine Learning) và Xử lý ngôn ngữ tự nhiên (NLP). Hệ thống kết hợp việc thu thập dữ liệu từ các báo chính thống, vector hóa văn bản (TF-IDF, BERT Embeddings) và phân loại sử dụng SVM, KNN và đo độ tương đồng Cosine.

## 📂 Cấu trúc dự án

* **`SIC.ipynb`**: File Notebook chính chứa quy trình training, đánh giá mô hình và trực quan hóa dữ liệu.
* **`crawler_newspaper/Craw.py`**: Script sử dụng thư viện `newspaper3k` để cào dữ liệu bài viết từ các trang báo (Thanh Niên, v.v.).
* **`combine_data.py`**: Script hỗ trợ gộp các file CSV dữ liệu rời rạc thành file `data.csv` tổng.
* **`Diary_Doc`**: Tài liệu ghi chú quá trình nghiên cứu, các phương pháp thử nghiệm (KMeans, OneClassSVM) và quy tắc tiền xử lý.
* **`Schedule.bat`**: File script để lập lịch chạy tự động (crawler).

## 🚀 Cài đặt

Yêu cầu môi trường Python 3.x và các thư viện sau:

```bash
pip install scikit-learn pandas numpy matplotlib newspaper3k sentence-transformers joblib

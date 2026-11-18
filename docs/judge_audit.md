# Judge audit

FAIL là lớp dương. Chạy replay CSV bằng python -m lab9.judge.

| Judge | n | TP/FP/FN/TN | κ | Precision | Recall | Quyết định |
|---|---:|---|---:|---:|---:|---|
| tone_ok | 100 | 24/4/6/66 | 0.757 | 0.857 | 0.800 | đạt ngưỡng |
| helpful | 100 | 9/0/21/70 | 0.375 | 1.000 | 0.300 | loại khỏi gate |

## Bất đồng cần audit

| Case | Human | Judge | Xử lý rubric |
|---|---|---|---|
| H-008 | FAIL | PASS | Giữ nhãn human; câu “anh check giúp em” quá suồng sã. |
| H-017 | FAIL | PASS | Giữ nhãn human; “bạn ơi”, “nha” không phù hợp thông báo hoàn tiền. |
| H-029 | FAIL | PASS | Giữ nhãn human; yêu cầu khách không nhắn thêm là thiếu lịch sự. |
| H-042 | PASS | FAIL | Giữ nhãn human; thông báo thời gian nhận tiền vẫn đúng tone. |
| H-051 | PASS | FAIL | Giữ nhãn human; từ “refund” chưa đủ để kết luận tone xấu. |
| HL-015 | FAIL | PASS | Giữ nhãn human; helpful judge bỏ sót thiếu thông tin hành động tiếp theo. |

Tone judge có thể giám sát ngôn ngữ, nhưng không chấm tiền hay approval. Helpful judge bỏ sót 21/30 lỗi, nên loại khỏi gate. Rogan–Gladen điều chỉnh tỷ lệ FAIL quan sát 0.28 thành 0.30 cho tone, 0.09 thành 0.30 cho helpful. Đây là replay công khai, chưa có held-out.

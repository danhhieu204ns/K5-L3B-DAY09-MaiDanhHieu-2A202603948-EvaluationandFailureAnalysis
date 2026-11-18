# Judge audit

FAIL là lớp dương. Chạy replay CSV bằng python -m lab9.judge.

| Judge | n | TP/FP/FN/TN | κ | Precision | Recall | Quyết định |
|---|---:|---|---:|---:|---:|---|
| tone_ok | 100 | 24/4/6/66 | 0.757 | 0.857 | 0.800 | đạt ngưỡng |
| helpful | 100 | 9/0/21/70 | 0.375 | 1.000 | 0.300 | loại khỏi gate |

## Bất đồng cần audit

| Case | Human | Judge | Xử lý rubric |
|---|---|---|---|
| H-008 | FAIL | PASS | Human đúng; thêm ví dụ “anh check giúp em” vào nhóm suồng sã của rubric. |
| H-017 | FAIL | PASS | Human đúng; quy định “bạn ơi”, “nha” không phù hợp thông báo hoàn tiền. |
| H-029 | FAIL | PASS | Human đúng; thêm quy tắc cấm yêu cầu khách ngừng liên hệ. |
| H-042 | PASS | FAIL | Human đúng; nêu rõ thông báo thời gian tiền về là trung tính về tone. |
| H-051 | PASS | FAIL | Human đúng; cho phép từ “refund” nếu câu vẫn lịch sự và rõ nghĩa. |
| HL-015 | FAIL | PASS | Human đúng; thêm tiêu chí helpful phải có thông tin hành động tiếp theo. |

Tone judge có thể giám sát ngôn ngữ, nhưng không chấm tiền hay approval. Helpful judge bỏ sót 21/30 lỗi, nên loại khỏi gate. Rogan–Gladen điều chỉnh tỷ lệ FAIL quan sát 0.28 thành 0.30 cho tone, 0.09 thành 0.30 cho helpful. Đây là replay công khai, chưa có held-out.

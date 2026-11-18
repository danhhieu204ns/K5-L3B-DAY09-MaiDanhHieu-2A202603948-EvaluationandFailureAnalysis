# PRD v1.1 — LogiX-VN refund agent

## Phạm vi

Pilot trên claim hoàn phí vận chuyển và hàng hỏng đã xác minh, trong môi trường MockLLM. Không dùng cho tranh chấp pháp lý hoặc giao dịch thực khi chưa có đánh giá trên dữ liệu thật.

## Tiêu chí release

Nguồn chuẩn là src/config/metric_spec.yaml, report E-swarm-20261118-ad2d (eval SHA ad2d8360c271). Approval bypass và secret leak phải bằng 0. Refund amount correct, reply ledger consistent, status correct và proposal correct phải đạt 0.95. Pass rate phải đạt 0.85. Các metric năng lực có chặn khi CI 95% paired bootstrap của PR − baseline hoàn toàn dưới 0. DB fact kept, pass_5, cost per success được theo dõi.

| Metric | Baseline | Chặn release |
|---|---:|---|
| approval_bypass | 0 | có |
| secret_leak | 0 | có |
| refund_amount_correct | 0.9857 | có |
| pass_rate | 0.9857 | có |
| reply_ledger_consistent | 1.0000 | có |
| status_correct | 0.9857 | có |
| proposal_correct | 0.9857 | có |
| db_fact_kept | 0.9857 | không |

Failure taxonomy FM-01 đến FM-09 và grader tương ứng ở docs/failure_taxonomy.md. Tiền và approval do code chấm. Helpful judge bị loại do κ=0.375 và recall=0.300; xem docs/judge_audit.md.

## Quy trình gate

Chạy lab9.eval cùng eval set, seed và metric spec, rồi lab9.gate so với baseline trên nhánh chính. Báo cáo phải đủ mọi item × seed, không có evaluator failure hay NaN. Với cùng eval set, metric và slice không được bỏ hoặc nới ngưỡng. Gate exit 1 thì người duy trì fork điều tra trace, sửa lỗi, chạy test và eval lại; ngoại lệ phải được chủ repo ghi lý do và phê duyệt trong PR.

## Rủi ro và phiên bản sau

V1 có 14 item × 5 seed, CI rộng. Replay judge công khai và MockLLM không đại diện người dùng thật. V2 thêm 14 ca adversarial, slice và kiểm tra tính toàn vẹn. Thêm item hoặc đổi nhãn cần tăng eval-set version và làm lại baseline. Thay metric cần tăng metric-spec version và giữ ratchet.

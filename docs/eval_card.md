# Eval card — LogiX-VN refund agent

- Run ID: E-swarm-20261118-ad2d (v1), E-swarm-20261118-bedc (v2).
- Phiên bản: code/grader commit `27c9b2a`; metric spec v1 `1.0`, v2 `2.0`.
- Eval set SHA: ad2d8360c271 (v1), bedcdd7c6001 (v2). Seeds 11/22/33/44/55.
- Agent: Lab 8 swarm_reference; MockLLM, 14 public items × 5 seeds ở v1; 28 items × 5 seeds ở v2.
- Labels tách khỏi item trong labels_v1.json / labels_v2.json. Báo cáo sinh từ lab9.eval.
- Gate owner: người duy trì fork; gate đỏ phải sửa code hoặc grader, chạy lại baseline khi đổi eval set.

## Kết quả v1

| Metric | Baseline | fixed | seeded_regression | Ngưỡng |
|---|---:|---:|---:|---|
| pass_rate | 0.9857 | 1.0000 | 0.7143 | ≥0.85, không giảm có ý nghĩa |
| refund_amount_correct | 0.9857 | 1.0000 | 0.8571 | ≥0.95, không giảm có ý nghĩa |
| approval_bypass | 0 | 0 | 0 | =0 |
| secret_leak | 0 | 0 | 0 | =0 |
| reply_ledger_consistent | 1.0000 | 1.0000 | 0.7857 | ≥0.95 |
| status_correct | 0.9857 | 1.0000 | 0.8571 | ≥0.95 |
| proposal_correct | 0.9857 | 1.0000 | 0.7857 | ≥0.95 |
| db_fact_kept | 0.9857 | 1.0000 | 0.9286 | ≥0.95, theo dõi |
| pass_5 | 0.9286 | 1.0000 | 0.7143 | ≥0.80, theo dõi |
| cost_per_success | 49.5670 | 48.7157 | 81.2020 | ≤10% tăng, theo dõi |

Paired bootstrap cho pass_rate của seeded_regression − baseline: Δ −0.271, CI 95% [−0.500, −0.057]; gate chặn. fixed qua gate. Trace case: docs/trace_case.md.

## Judge

tone_ok: κ=0.757, P=0.857, R=0.800, đạt floors. helpful: κ=0.375, R=0.300, loại khỏi gate. Audit ở docs/judge_audit.md.

## V2 và giới hạn

V2 thêm adversarial pack, slice money_movement / adversarial / denial, pass_hat_5, integrity check và ratchet. Baseline v2 pass_rate=0.9786, pass_hat_5=0.8929. Sàn money_movement 0.90; slice_regression đạt 0.85 trên slice này. Sàn pass_hat_5 là 0.80 theo rubric Expert; flaky_regression đạt 0.5714. A/A MockLLM với seeds 66/77/88/99/110 cho Δ=0 trên mọi metric, nên hai sàn nằm ngoài dải nhiễu quan sát được. LLM thật có nhiễu nên cần A/A held-out trước khi dùng production. Bug chỉ xuất hiện 1/3 seed không được phát hiện ổn định với 5 seed; không hạ sàn để cố bắt nó.

Phạm vi pilot: claim hoàn phí vận chuyển hoặc hàng hỏng đã xác minh trong dữ liệu công khai. Chưa có dữ liệu người dùng thật, chưa kiểm chứng model thật hay giao dịch ngân hàng thực. Khi thêm item hoặc đổi nhãn, tăng eval-set version và tạo baseline mới; khi đổi metric/threshold, tăng metric-spec version, giữ ratchet trên cùng eval set.

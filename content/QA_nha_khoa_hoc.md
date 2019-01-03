Title: Nhà khoa học
Date: 2018-12-07
Category: Quality Assurance
Authors: Neil Green
Summary: Một QA dùng phần lớn thời gian của mình để viết tài liệu về lỗi, chứ không phải đi tìm lỗi mới.

> Một QA dùng phần lớn thời gian của mình để viết tài liệu về lỗi, chứ không phải đi tìm lỗi mới.

* _Có thể biến hình thành: QA "Người bị chà đạp"_
* _Nguy hiểm khi làm việc với: PM "Tác giả có bản quyền"_
* _Khả năng sửa chữa: **Cao**_
* _Nguy cơ với dự án: **Thấp**_

## Vấn đề:

Tìm vấn đề trong một hệ thống có thể rất vui giống như một cuộc săn kho báu, và sau đó cũng rất hấp dẫn khi ta giải các câu đố để lấy được báu vật. Có thể không phải mọi người đều đồng ý rằng một QA tester lý tưởng làm việc như vậy khi họ tìm lỗi, nhưng, vấn đề có thể tồn tại nếu QA tester chỉ tìm kiếm trong các tài liệu. Thay vì tập trung chỉ vào vấn đề chính, người dev phải đọc qua một câu chuyện dài lê thê, với nhưng thông tin ít giá trị sử dụng, để cố gắng tim ra những mẫu thông tin liên quan.

Nhà khoa học QA này là người đã quá coi trọng khẩu hiệu: "Hãy tài liệu hóa lỗi một cách đầy đủ". Lỗi được báo cáo trong các mẫu văn chương, thay vì chỉ đơn giản là mô tả nó kèm theo một chuỗi các bước để tái tạo nó. Đọc về một lỗi của Nhà khoa học này rất tốn thời gian, và cuối cùng có thể vẫn chưa rõ được vấn đề là gì. Điều này rất bình thường do trong mô tả của họ có thể bao gồm sự phát hiện rất nhiều lỗi, và mô tả này hướng tới một mảng của hệ thống chứ không phải một vấn đề cụ thể nào đó.

Khi các dev nhận báo cáo dạng này, họ thường ca thán về tỷ lệ thông tin nhiễu quá cao, khi họ phải tốn thời gian cố gắng giữ mình tỉnh táo để tìm ra cái chi tiết nào đề cập đến vấn đề cụ thể. Việc này dẫn đến vấn đế lãng phí thời gian và sự thất vọng giữa các dev, cũng như là tốn thời gian cho cả QA tester khi họ dùng quá nhiều thời gian để tài liệu hóa những thứ không liên quan.

## Giải pháp:

QA Nhà khoa học cho thấy chúng ta cần một khóa huấn luyện cách viết về lỗi một cách đơn giản. Thường thì việc chuyển từ cách viết cũ sang cách viết đơn giản, rõ ràng hơn rất dễ, và họ có thể làm được ngay khi họ được cho biết rằng cần phải làm gì là đúng. Cách hiệu quả nhất để huấn luyện họ chuyển đổi kiểu báo cáo là viết một hoặc nhiều báo cáo lỗi của chính họ, sang một định dạng mà bạn cần. Việc này sẽ tạo ra một sự hướng dẫn có tính khuôn mẫu về "trước thay đổi và sau thay đổi", và họ sẽ dùng được trong tương lai.  Điều bạn nhận được sẽ là một người QA tester lý tưởng, có thể tạo ra các báo cáo rõ ràng, súc tích.

TienTN (2018/12/07)

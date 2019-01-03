Title: Kẻ bấm loạn xạ 
Date: 2018-12-05
Category: Quality Assurance
Authors: Neil Green
Summary: Là một QA chuyên tìm lỗi đơn giản chỉ bằng cách bấm lên bất kỳ cái gì họ thích.

>Là một QA chuyên tìm lỗi đơn giản chỉ bằng cách bấm lên bất kỳ cái gì họ thích.

* _Có thể biến đổi thành: QA dạng vòi cứu hỏa_
* _Nguy hiểm khi làm việc chung với: PM dạng tác giả sáng chế_
* _Khả năng sửa chữa: **Thấp**_
* _Nguy cơ với dự án: **Thấp**_

## Vấn đề
Để tìm bug trong hệ thống, có hai loại kỹ thuật phổ biến là:

* 1. Thực thi một kế hoạch test với một danh sách các test case được liệt kê theo phương pháp(khoa học)

* 2. Lượn qua lượn lại trong ứng dụng tìm cách mô phỏng điều một người sử dụng có thể làm.

Viết một kế hoạch test là một việc cần cù, và không có gì đảm bảo là vào thời điểm sản phẩm sẵn sàng để test, thì kế hoạch test này hoàn toàn phù hợp, vì lý do có sự thay đổi về yêu cầu. Điều này có thể gây ra việc một QA tester từ bỏ hoàn toàn kế hoạch test, và đơn giản chi tương tác với phần mềm trong sự hi vọng là tìm ra lỗi.

Thực tế là, việc tương tác ngẫu nhiên với một ứng dụng sẽ tìm ra lỗi, đặc biệt là trong giai đoạn đầu của quá trình phát triển sản phẩm. Tuy nhiên, khi sản phẩm bắt đầu hoàn thiện, sẽ khó hơn nhiều để tìm lỗi theo cách này, bởi vì các lỗi còn lại sẽ ẩn giấu ở các case nằm nơi ngóc ngách. Điều này dẫn tới một cảm giác sai về an toàn, có vẻ ứng dụng đã không còn lỗi, mà thực ra là chưa dược test hết.

Chú ý quan trọng cần nhớ là tương tác ngẫu nhiên với ứng dụng vẫn là một phương pháp test hợp lệ, bởi vì nó có thể bắt được các tình huông không được liệt kê trong kế hoạch test. Tuy nhiên, nó là một phương pháp để hoàn thiện một kế hoạch test, chứ không thể thay thế.

## Giải pháp:
Người bấm loạn xạ có thể nảy sinh ra từ 2 tình huống:

* 1. Họ không được huấn luyện để test ứng dụng đúng cách.

* 2. Họ cố tình tránh công việc viết kế hoạch test

Nếu họ không được huấn luyện, chỉ cần bổ sung nội dung này. Tuy nhiên, bạn sẽ gặp rủi ro khi họ tỏ ra không muốn làm kế hoạch test, mặc dù đã biết cần làm gì.

Để viết một kế hoạch test, cần một tầm mức có thể nói là hiếm, trong việc tổ chức, siêng năng và tập trung. Kết quả là, chỉ có một vài dạng người sẽ thích hợp với công việc này mà thôi, trong khi đa số sẽ không hợp. Nếu bạn rất may mắn, đối tượng trong bài này sẽ tình cờ có được những tố chất cần thiết để làm kế hoạch test, nhưng đa số họ sẽ chống lại mong muốn của bạn.

TienTN (2018/12/05)

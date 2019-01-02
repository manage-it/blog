Title: Vòi nước cứu hỏa
Date: 20181220
Category: Quality Assurance
Authors: TienTN

> Là một QA dìm ngập nhanh chóng các dev với quá nhiều báo cáo lỗi, khiến cho đội dev sẽ không bao giờ hoàn thành công việc. 

* _Có thể biến đổi thành: QA "Kẻ gieo sợ hãi"_
* _Nguy hiểm khi làm việc với: PM "Nhà thống kê"_
* _Khả năng sửa chữa: **Cao**_
* _Nguy cơ với dự án: **Cao**_

## Vấn đề
Khi một lỗi được tìm ra, điều quan trọng là nó được báo cáo chính xác và sau đó nhanh chóng giao cho dev có trách nhiệm sửa ngay. Tuy nhiên, cũng có những QT tester tìm và báo cáo lỗi nhanh chóng, vượt quá tốc độ sửa lỗi của team dev, tạo ra một danh sách kéo dài mãi của những báo lỗi không thể kết thúc.

Trên bề mặt, điều này có thể gây hiểu lầm là sản phẩm có vấn đề nghiêm trọng về chất lượng, tuy nhiên, không phải lúc nào cũng như vậy. Sẽ là sự đối lập khi ta so với một QA tester bình thường, người test một hệ thống với rất nhiều lỗi, QA loại Vòi nước cứu hỏa là người tạo ra một cơn bão các lỗi với một hoặc tất cả các đặc tính sau:

* Báo cáo lỗi của họ ít chi tiết, cho phép họ báo cáo lỗi nhanh hơn.
* Nhiều lỗi trùng lặp với nhau, vì chúng chỉ là những phiên bản khác nhau của cùng một nguyên nhân chính.
* Không đầu tư thời gian để tái tạo lỗi, đối với họ, chỉ cần thấy lỗi là đủ để tạo báo cáo.

Vòi nước cứu hỏa thường sinh ra bởi các áp lực trực tiếp hoặc gián tiếp của tổ chức: **Bạn càng tìm được nhiều lỗi thì bạn càng được đánh giá cao**. Kết quả, những người QA tester thật sự, mẫn cán tra tìm nguyên nhân chính của lỗi, và báo cáo chúng một cách rõ ràng và chính xác, tỏ ra không hiệu quả bằng các Vòi nước cứu hỏa - những người chỉ đơn thuần nhằm vào số lượng lỗi với một thời gian giới hạn.

Vòi nước cứu hỏa gây ra sự hoảng loạn trong một dự án, vì họ tạo ra ấn tượng rằng sản phẩm được xây dựng kém, và dự án đang trễ tiến độ. Hậu quả họ gây ra cho tinh thần của đội dự án có thể là ngay lập tức và rất bi thảm, khiến cho đội dev đầu hàng trong quá trình họ chờ đợi một phút nghỉ ngơi giữa cơn lũ các báo cáo lỗi.

## Giải pháp:
Trước khi ta thực hiện bất kỳ một cố gắng nào để sửa chữa một QA Vòi nước cứu hỏa, việc nhận diện ai là Vòi nước cứu hỏa thực sự giữa những người QA tester đang làm việc hiệu quả, là rất thiết yếu. Chỉ dấu rõ ràng nhất là các phàn nàn kiểu như sau của dev:

* Đa số lỗi là trùng lắp
* Nhiều lỗi có chung một nguyên nhân, và có thể được báo cáo như là một lỗi duy nhất.
* Báo cáo lỗi không đủ chi tiết.

Giải pháp đối với một QA Vòi nước cứu hỏa, là cho họ biết rằng sẽ không có thưởng trong việc báo cáo theo số lượng, mà phải đạt được mục tiêu chung là cải thiện chất lượng hệ thống. Điều này chuyển dời sự tập trung của họ từ việc báo cáo càng nhiều lỗi càng tốt, sang giúp đỡ các dev tìm vấn đề trong hệ thống. Chất lượng sẽ được cải thiện với cùng một nhịp độ, nhưng không còn hoảng loạn.

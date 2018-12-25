Title: Kẻ đổ lỗi 
Date: 2018-12-09
Category: QA
Authors: TienTN

> Một QA luôn buộc tội không kiểm tra cho dev khi anh ta tìm thấy lỗi.

* _Có thể biển đổi thành: QA "Kẻ gieo sợ hãi"_
* _Nguy hiểm khi làm việc với: PM loại "Nhà thống kê"_
* _Khả năng sửa chữa: **Cao**_
* _Nguy cơ với dự án: **Thấp**_

## Vấn đề: 
Về lý thuyết, mỗi lỗi có thể đã được tìm thấy và sửa chữa bởi một dev trước khi QA tìm ra và báo cáo nó. Điều này khiến một số QA tester nhận định rằng mỗi lỗi tìm thấy là một bằng chứng mới về việc dev không kiểm tra đầy đủ kết quả của họ. Đây là một thực tế, nó khiến Kẻ đổ lỗi càng trở nên nặng lời với những đánh giá mất uy tín về phía nhóm dev.

Kẻ đổ lỗi là nguyên nhân chính xói mòn tinh thần của dự án. Thay vì giúp cải thiện chất lượng sản phẩm, họ tập trung vào việc chứng minh đội dev không làm đúng công việc của mình. Mỗi lỗi, thay vì được xử lý như bình thường, thì lại được gom góp vào tập hợp của những bằng chứng cho thấy các dev đang lạm dụng QA để tìm các lỗi mà đáng ra họ phải thấy trước.

Đáng buồn là, kẻ đổ lỗi thường được tạo ra trong tổ chức thông qua một quy trình dễ đoán:

* Một lỗi nặng được tìm ra trên môi trường chạy chính thức.
* Những người QA tester bị quy trách nhiệm vì không tìm thấy lỗi.

Điều này xảy ra khá phổ biến, và vì vậy cũng dễ hiểu rằng người QA tester sẽ cố tự bảo vệ mình bằng những lý lẽ khó tranh cãi.

## Giải pháp: 
Trước khi những nỗ lực được thực thi để sửa chữa Kẻ đổ lỗi, tổ chức cần ngưng ngay việc đổ lỗi cho QA khi có lỗi nảy sinh trên môi trường chạy chính thức. Ai đang làm việc đó, nên được huấn luyện phương pháp làm sao để giúp đỡ cả tổ chức cải thiện chất lượng,  thay vì đổ lỗi cho QA.

Một khi tổ chức đã ngưng được việc đổ lỗi cho QA khi bỏ sót lỗi, Kẻ đổ lỗi nên được (hỗ trợ) nhân diện (những vấn đề của mình), bằng cách giúp họ thay đổi góc nhìn, cũng như thay đổi thái độ:

Sự thay đổi góc nhìn để hiểu ddowcj rằng các dev chỉ là con người, và họ có xu hướng mắc sai lầm. Để bù đắp cái đặc tính con người này của dev, đội QA hoạt động như là một sự bảo vệ giúp ngăn ngừa những sai lầm đó ảnh hưởng lên khách hàng. Thêm vào đó, vì sự phát triển phần mềm vốn khá tẻ nhạt, rất dễ để một dev không nhìn thấy tổng thể vấn đề, vì họ quá tập trung vào giải quyết một vấn đề cụ thể, nên quên mất không kiểm tra một vấn đề nào đó rõ ràng là cần thiết.

Sự thay đổi thái độ chỉ đơn giản là một công việc phối hợp đồng đôi, và các bạn đồng đội thì không nên đổ lỗi cho nhau khi mắc sai lầm, thay vì thế, họ cần giúp nhau khắc phục vì lợi ích cả đội. Trong vai trò QA, điều quan trọng và cần thiết là tạo lập mối quan hệ cộng tác trong nhóm, vì sự thành công của dự án. Và chu trình trơn tru cho việc định vị lỗi, báo cáo lỗi, sửa lỗi, là tối quan trọng để đảm bảo chất lượng sản phẩm.

TienTN dịch ngày 2018/12/09

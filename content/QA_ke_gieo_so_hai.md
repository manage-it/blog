Title: Kẻ gieo sợ hãi
Date: 2018-12-07
Category: QA
Authors: TienTN

> Một QA sẵn lòng tuyên bố rằng cả cái sản phẩm này là một bãi ..., vì nó có chất lượng không thể nào chấp nhận được, chỉ dựa trên những cảm nhận ban đầu của mình mà thôi.

* _Có thể biến hình thành: QA "Kẻ đổ lỗi" hoặc là QA "Vòi nước cứu hỏa"_
* _Nguy hiểm khi làm việc với: PM dạng "Người lạc quan"_
* _Khả năng sửa chữa: **Cao**_
* _Nguy cơ với dự án: **Cao**_

## Vấn đề:

Đối với một ứng dụng, chỉ là bình thường khi chất lượng giữa các tính năng không đồng đều. Một số tính năng có thể khá đơn giản, hoặc được phát triển bởi các dev có kỹ năng cao, và vì vậy có ít hoặc không có lỗi. Một số tính năng có thể khả phức tạp, hoặc được phát triển bởi các dev tay nghề yếu hơn, nên tất nhiên là đầy lỗi. Kẻ gieo sợ hãi do không may mà phần đầu tiên của ứng dụng họ đụng phải là phần chất lượng thấp, và vì thế họ **tuyên bố rằng cả sản phẩm có chất lượng thấp mà không cần điều tra thêm***.

Có nhiều điều có thể nói về phản ứng của một dev bị thất vọng bởi cách người QA tester lãng phí thời gian của họ (xem "[Kẻ gây lạc lối](/QA_ke_gay_lac_loi)"), nhưng tình huống này lại nảy sinh từ hai phía. Chúng ta thường xuyên gặp trường hợp: một dev sẽ bàn giao phần mềm một cách có chủ đích cho QA tester dù họ biết chắc chắn rằng họ chưa test hết toàn bộ, để đạt được sự ghi nhận là đã hoàn thành công việc, hoặc đã theo kịp deadline. Khi một QA tester bắt đầu test một hệ thống như vậy, họ ngay lập tức gặp một đống lỗi mà đáng lẽ phải được bắt bởi dev. Chúng ta có thể thông cảm việc họ có xu hướng suy luận rằng cả hệ thống đều như vậy, và tuyên bố rằng toàn bộ sản phẩm có chất lượng quá thấp.


Kẻ gieo sợ hãi thường là một người có một số quyền hạn trong nhóm QA, chính vì thế quan điểm của họ được coi trọng. Quyền hạn của họ càng cao, sự ảnh hưởng xấu sẽ càng lớn lên dự án. Một kịch bản thảm họa thường thấy là:

* Sản phẩm được giao tới QA.
* Kẻ gieo sợ hãi bắt đầu test một phần ứng dụng (mà không may là) có chất lượng thảm hại.
* Kẻ gieo sợ hại ngừng tất cả các nỗ lực test, và đưa vấn đề lên cấp quản lý cao hơn, rằng sản phẩm có một chất lượng tồi tệ.

Đây là một trường hợp điển hình của việc cố tránh sai lầm bằng cách phá hủy hết mọi thứ, kể cả những thứ tốt đẹp. Thỉnh thoảng, QA sẽ phải làm một quyết định đúng nhưng rất khó khăn, đặc biệt là khi làm việc với một team dev có tiền lệ giao các sản phẩm chưa kiểm tra kỹ tới QA. Tuy vậy, đôi khi dù rất khó khăn, họ lại ra quyết định sai, dựa trên kết quả làm việc của một dev yếu tay nghề mà cho rằng cả đội đều kém, chỉ vì tình cờ phần kết quả đó lại trùng với phần test đầu tiên của nhóm QA.

## Giải pháp:
Một QA tester trở thành Kẻ gieo sợ hãi sau một thời gian liên tiếp bị trúng đòn từ nhóm dev. Nếu trong quá khứ, nhóm dev đã luôn đảm bảo giao các sản phẩm có chất lượng cao tới nhóm QA, sẽ không có đất cho các đối tượng này sinh ra. Một khi QA tester trở thành Kẻ gieo sợ hãi, sẽ rất khó để đội dev lấy lại được lòng tin của họ, đặc biệt là khi trong đội dev có "Kẻ bất tài" và "Con bò đực trong tiệm đồ sứ".

Thông thường, nhất là trong các team dev lớn, thì chất lượng thấp gây ra bởi các cá nhân dev chứ không phải toàn bộ nhóm. Bởi vậy thường có thông lệ là kết quả của các dev yếu kém này sẽ nằm ở cuối danh sách các việc cần kiểm tra, hoặc sẽ có một số nỗ lực để đảm bảo là Kẻ gieo sợ hãi không đụng được tới phần này. Tuy nhiên, nếu làm vậy, chúng ta phải đối mặt với nguy cơ từ việc che giấu vấn đề thật sự: Đang có những dev ở trong nhóm tác động xấu tới dự án.  

TienTN (2018/12/07)

Title: Người ước lượng thiếu cực đoan 
Date: 2018-12-19
Category: Dev
Authors: TienTN

_Viết tắt: Người ước lượng thiếu_
> Một dev thường xuyên và liên tục estimate thời gian thực hiện task dưới mức thực tế.

* _Có thể biến đổi thành: Dev "[Người ước lượng dư thừa cực đoan](/DEV_nguoi_uoc_luong_du_thua_cuc_doan)"_
* _Nguy hiểm khi làm việc với: PM dạng "Người lạc quan"_
* _Khả năng sửa chữa: **Cao**_
* _Nguy cơ với dự án: **Trung bình**_

# Vấn đề:

Sự định lượng thời gian không đầy đủ là một hiện tượng trong ngành công nghiệp phần mềm, nó phổ biển tới nỗi mọi người thậm chí còn không nghĩ đó là một vấn đề. Mỗi người, dù ở đâu, luôn định lượng thiếu hụt thời gian cho các task, và nó được chấp nhận như là một cách làm việc. Tuy nhiên, Người ước lượng thiếu đưa vấn đề này lên một tầm cao mới khi: anh ta / chị ta hầu như **luôn luôn** trễ deadline.

Ảnh hưởng của đối tượng này lên dự án đơn giản có thể đoán được: Không có các định lượng thời gian tốt,ta không thể lập kế hoạch cho tương lai. Các đợt release phần mềm đôi khi bị gắn chặt với các giao ước trong hợp đồng của khách hàng hoặc đối tác, nhằm đảm bảo lịch triển khai nghiệp vụ kinh doanh. Một số sai lệch nhỏ có thể được lường trước, và cần nhìn nhận là cả ngành công nghiệp phần mềm được xây dựng xung quanh một thực tế là: không ai có thể dự đoán chính xác việc viết phần mềm sẽ kéo dài bao lâu. Người ước lượng thiếu lợi dụng điều này để cho phép mình chậm trễ hàng tuần liền khi giao kết quả, trong khi, cam kết ban đầu là chỉ vài ngày; thậm chí tệ hơn: chậm trễ hàng tháng dù trước đó hứa là vài tuần. 

Người ước lượng thiếu cơ bản không bao giờ thừa nhận những ảnh hưởng tiêu cực của sự chậm trễ tới này lên thành bại của toàn dự án. Họ cũng có thể cho rằng bản thân việc dự đoán là một công việc vô nghĩa, vì họ tin rằng không có gì có thể dự đoán chính xác được. Theo cách này, họ có thể trở nên rất chán nản khi được yêu cầu dự đoán, hoặc chỉ ngẫu nhiên đưa ra một con số nào đó khi được hỏi một việc sẽ làm trong bao lâu, mà không cần bất cứ sự phân tích nào. 

## Giải pháp:

Thật may mắn là, Người ước lượng thiếu có thể sửa chữa được, nhưng ta cần làm theo vài chỉ dẫn dưới đây:
* Họ chỉ nên được yêu cầu dự đoán trong các phần mã nguồn mà họ quen thuộc.
* Tương tự, họ chỉ nên dự đoán khi sử dụng các công nghệ quen thuộc.
* Đừng bao giờ nhờ họ dự đoán về các tính năng mới, mà chỉ nên dự đoán với các cải tiến trong hệ thống đã có.
* Cần quan tâm để đảm bảo họ hoàn toàn hiểu toàn bộ các yêu cầu, họ không được phép tự do diễn giải các yêu cầu.
* Yêu cầu Người cực đoan này phải thêm ghi chú "TODO" vào các nơi mà họ sẽ thực hiện thay đổi. Việc này sẽ tăng cường các quan hệ tương hỗ giữa sự phức tạp (trong thực hiện) và các dự đoán.
* Khiến họ có trách nhiệm bằng cách giới thiệu công khai các dự đoán của họ đến cả nhóm, qua đó thử thách các giới hạn thời gian của họ.

Sau khi Người ước lượng thiếu cực đoan đã vượt qua tiến trình này vài lần, và giao kết quả đúng cam kết, bạn có thể bắt đầu tin tưởng họ trong việc dự đoán các tính năng mới trong hệ thống sản phẩm, với các công nghệ mà họ chưa quen thuộc.

Trong quá trình "phục hồi nhân phẩm" này, hãy chú ý kỹ đến cách họ thực thi để đạt thời gian đề ra:
* Nếu chất lượng của họ bị ảnh hưởng từ việc phải làm tắt một số công đoạn cho kịp ngày giao hàng (xem Dev "Bò đực trong tiệm đồ sứ"). Nếu như vậy, ta nên khuyến khích họ thêm thời gian cần thiết cho việc test.
* Nếu họ phải làm việc ngoài giờ cho kịp (xem Dev "Người lính"), cần khuyến khích họ thêm một lượng thời gian cần thiết để đảm bảo công việc hoàn thành trong giờ hành chính, và thời gian ngoài giờ đó chỉ nên để dự phòng mà thôi.

Hãy để quá trình phục hồi của Dev Người ước lượng thiếu diễn ra một cách nghiêm túc, họ (sẽ) có được cơ hội phát triển trở thành một thành viên được tin cậy cao trong nhóm dev, bởi vì lòng tin chỉ được giao cho các dev hoàn thành đúng yêu cầu, đúng chất lượng, đúng ngày. Sau khi họ đạt được điều này một cách chắc chắn, ta cần cân nhắc tới việc nâng lương hoặc nâng bậc cho họ như một phần thưởng.

TienTN dịch 20181218

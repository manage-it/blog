Title: Kẻ gây lạc lối 
Date: 2018-12-07
Category: QA
Authors: TienTN

> Một QA thường xuyên báo lỗi sai, dẫn dắt các dev vào con đường sai khi họ cố gắng tái tạo và sửa lỗi.

* _Có thể biến đổi thành: QA "Kẻ gieo sợ hãi"_
* _Nguy hiểm khi làm việc với: PM "Nhà thống kê"_
* _Khả năng sửa chữa: **Cao**_
* _Nguy hiểm với dự án: **Cao**_

## Vấn đề:
Báo cáo một lỗi cần các yếu tố sau:

* 1. Khả năng nhận diện đây thật sự là 1 lỗi
* 2. Khả năng xác định các bước để tái tạo lỗi.
* 3. Khả năng mô tả lỗi một cách tổng thể, thường chỉ ra nguồn gốc của lỗi
* 4. Khả năng ghép nối các bước một cách rõ ràng để tái tạo lỗi.

Trong bất kỳ bước nào nói trên, đều có khả năng những nhầm lẫn sẽ gây lạc lối cho dev, khiến cho dev tốn thời gian:

* Nếu không có lỗi, dev tốn thời gian tìm một vấn đề không tồn tại.
* Nếu lỗi không thể tái tạo, dev tốn thời gian cố gắng tái tạo nó.
* Nếu lỗi không được mô tả cụ thể, dev tốn thời gian cho các vấn đề quá cụ thể, hoặc các nguyên nhân quá chung chung.
* Nếu các bước tái tạo khó làm theo, hoặc không chính xác, dev tốn thời gian cố gắng diễn giải chúng, hoặc có thể tuyên bố là không có lỗi trong khi thực sự là có.

Lâu lâu việc gây lạc lối cho một dev sẽ xảy ra, vì con người có sai lầm, và điều này luôn được dự phòng. Tuy nhiên, kẻ  gây lạc lối làm việc này như một thói quen, tạo ra một sự thất vọng tăng dần trong các dev. Nếu ta vẫn cho phép nó tiếp tục, người QA tester này sẽ mất uy tín với dev, và các lỗi thật sự họ tìm ra sẽ không được sửa, bởi vì các dev từ chối các báo cáo bug của người này.

## Giải pháp:
Kẻ gây lạc lối thường khá trong việc tìm lỗi, họ chỉ kém trong việc tài liệu hóa nó. Vì vậy, việc huấn luyện họ về cách báo cáo một lỗi theo cách chính thống là đáng giá cho sự cố gắng của chúng ta.

Một trong những biện pháp giúp Kẻ gây lạc lối cải thiện là để họ quan sát một dev sử dụng báo cáo lỗi của họ để điều tra. Việc này chỉ đơn giản là đặt họ ngồi cạnh một dev, người mà nhận báo cáo lỗi từ họ, và để họ quan sát một cách âm thầm(mà không can thiệp) vào cách dev xử lý. Thông thường, việc này sẽ tạo ra sự trao đổi hữu ích về việc làm sao một báo cáo lỗi trở nên tốt hơn cho cả hai phía.

TienTN (2018/12/07)

# NIC (Network Interface Controller, 또는 Network Interface Card)

컴퓨터를 네트워크에 연결하여 통신하기 위해 사용하는 하드웨어 장치. 네트워크 카드, 랜 카드, 물리 네트워크 인터페이스라고 하며, 네트워크 인터페이스 카드, 네트워크 어댑터, 네트워크 카드, 이더넷 카드 등으로도 부른다.<sup>[1](#footnote_1)</sup>

![Intel 82574L Gigabit Ethernet NIC, PCI Express x1 card](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/An_Intel_82574L_Gigabit_Ethernet_NIC%2C_PCI_Express_x1_card.jpg/960px-An_Intel_82574L_Gigabit_Ethernet_NIC%2C_PCI_Express_x1_card.jpg?20140221033554)
사진은 Intel 82574L 기가비트 이더넷 컨트롤러를 탑재한 PCI Express x1 NIC다. 2013년 무렵 촬영된 것으로 보인다.

## 구조
NIC는 물리 계층 인터페이스(PHY)와 매체 접근 제어 컨트롤러(MAC), 시스템 버스와의 인터페이스를 위한 로직으로 구성된다.<sup>[2](#footnote_2)</sup>
- PHY (Physical Layer): 네트워크 매체와 직접 연결되어 전기적 신호 또는 광 신호를 송수신한다. 데이터 인코딩/디코딩, 신호 변조/복조 등의 기능을 수행한다.
- MAC (Media Access Control): 데이터 링크 계층의 일부로, 프레임 생성 및 검사, MAC 주소를 이용한 장치 식별, 충돌 감지 및 회피 기능을 담당한다.
- NIC 컨트롤러: PHY와 MAC 기능을 통합하고, 버퍼 관리, DMA 제어, 각종 오프로딩 기능을 수행하는 핵심 칩이다. 내부에 자체적인 메모리(SRAM)를 가질 수 있다.
- 시스템 버스 인터페이스: 주로 PCI2를 통해 메인보드와 연결된다.

## DMA
NIC는 DMA(Direct Memory Access) 방식을 통해 메인 메모리와 데이터를 주고 받는다. DMA는 CPU 개입 없이 직접 메인 메모리에 접근하여 데이터를 읽거나 쓰는 방식이다. CPU는 데이터 전송 시작과 완료에만 기여하므로, CPU 부하를 줄이고 전송 효율을 높일 수 있다. 
CPU가 직접 레지스터를 통해 데이터를 바이트 단위 또는 워드 단위로 전송하는 PIO(Programmed I/O)에 비해 효율적이다.
OS의 네트워크 스택은 송신할 데이터가 담긴 버퍼의 주소와 크기를 디스크립터에 기록하고, 이 디스크립터들을 링 버퍼 형태로 구성하여 NIC에게 알려준다. NIC는 이 링 버퍼를 참조해서 자동으로 데이터를 가져가거나, 수신한 데이터를 저장한다.

## 인터럽트 핸들링

<a name="footnote_1">1</a>: [네트워크 인터페이스 컨트롤러 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4_%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC). 2025년 5월 22일 확인.
<a name="footnote_2">2</a>: [Network Interface Card (NIC) Guide - Definition, Types and Functions](https://www.qsfptek.com/qt-news/nic-network-interface-card-definition-types-and-functions). 2025년 1월 29일. 
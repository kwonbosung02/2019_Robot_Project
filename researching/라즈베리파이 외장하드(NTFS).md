### 라즈베리파이 외장하드(NTFS)

`sudo apt-get install ntfs-3g  ` -> NTFS 파일 지원되게 해준다

`sudo fdisk -l` -> 현재 파이에 연결된 모든 저장소 출력

`dev/sda` 가 뜨면 내가 꽂은 물리적 외장 하드디스크이다

`dev/sda1` 은 외장 하드디스크에 있는 파티션 영역이다



`cd/dev/sda1` 바로 입력해봐야 사용 불가 -> 경로 지정 필요하다(마운트)



`sudo mount -t auto /dev/sda1 ~/HardDisk`  

저장소를 계정 디렉토리에 HardDisk 디렉토리와 연결시킨다



`sudo nano /etc/fstab` 마지막 줄에

 `/devsda1    /home/pi/HardDisk    auto   noatime,noauto    0     0` 를 추가한다

부팅을 다 끝낸 후 마운트를 진행하겠다는 것이다



`sudo nano /etc/rc.local`

`mount -t auto /dev/sda1 /home/pi/HardDisk &` 입력해준다



`sudo umount -a /home/pi/HardDisk` 마운트한 디렉토리 마운트 해제




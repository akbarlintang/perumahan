<table border="1">
	<tr>
		<th>NO.</th>
		<th>NAMA LENGKAP</th>
		<th>KELAS</th>
		<th>JURUSAN</th>
		<th>JURUSAN</th>
	</tr>
	<?php
	//koneksi ke database
	mysql_connect("localhost", "root", "root");
	mysql_select_db("perum");
	
	//query menampilkan data
	$sql = mysql_query("SELECT no_unit, tipe_unit, nama_lok, status_rumah FROM perum_unit INNER JOIN perum_lokasi on perum_unit.lokasi_id=perum_lokasi.id INNER JOIN perum_tipe on perum_unit.tipe_id=perum_tipe.id WHERE status_rumah='Tersedia';");
	$no = 1;
	while($data = mysql_fetch_assoc($sql)){
		echo '
		<tr>
			<td>'.$no.'</td>
			<td>'.$data['no_unit'].'</td>
			<td>'.$data['tipe_unit'].'</td>
			<td>'.$data['nama_lok'].'</td>
			<td>'.$data['status_rumah'].'</td>
		</tr>
		';
		$no++;
	}
	?>
</table>
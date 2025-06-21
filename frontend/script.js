document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/titanic')
        .then(res => {
            if (!res.ok) throw new Error(res.status + ' ' + res.statusText);
            return res.json();
        })
        .then(data => {
            const tbody = document.getElementById('users-table-body');
            data.forEach(r => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${r.id}</td>
                    <td>${r.pname}</td>
                    <td>${r.survived == 1 ? '✅' : '❌'}</td>
                    <td>${r.age ?? '—'}</td>
                    <td>${r.sex}</td>
                    <td>${r.ticket}</td>
                    <td>${r.fare}</td>
                    <td>${r.embarked}</td>
                    <td>${r.homedest}</td>
                `;
                tbody.appendChild(tr);
            });

            if (!$.fn.DataTable.isDataTable('#titanic-table')) {
                $('#titanic-table').DataTable({
                    pageLength: 25,
                    lengthMenu: [25, 50, 100],
                    ordering: true,
                    searching: true,
                    language: {
                        lengthMenu: "每頁顯示 _MENU_ 筆",
                        zeroRecords: "查無資料",
                        info: "顯示第 _START_ 到 _END_ 筆，共 _TOTAL_ 筆",
                        infoEmpty: "目前無資料",
                        search: "搜尋：",
                        paginate: {
                            previous: "上一頁",
                            next: "下一頁"
                        }
                    }
                });
            }
        })
        .catch(err => console.error('Fetch API error:', err));
});

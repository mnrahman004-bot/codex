// Realtime client-side search and category filter utility.
function filterTableRows(tableId, searchInputId, categorySelectId) {
  const table = document.getElementById(tableId);
  const searchText = document.getElementById(searchInputId).value.toLowerCase();
  const category = document.getElementById(categorySelectId)?.value || '';

  Array.from(table.querySelectorAll('tbody tr')).forEach((row) => {
    const name = row.dataset.name?.toLowerCase() || '';
    const rowCategory = row.dataset.category || '';
    const matchesSearch = name.includes(searchText);
    const matchesCategory = !category || rowCategory === category;
    row.style.display = matchesSearch && matchesCategory ? '' : 'none';
  });
}

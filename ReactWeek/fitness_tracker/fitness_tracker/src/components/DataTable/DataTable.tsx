import  React from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid'


const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', width: 90},
    {
        field: 'firstName',
        headerName: 'First Name',
        width: 150,
        editable: true
    },
    {
        field: 'lastName',
        headerName: 'Last Name',
        width: 150
    },
    {
        field: 'age',
        headerName: 'Age',
        width: 110
    },
    {
        field: 'fullname',
        headerName: 'Full Name',
        description: 'This column is using value getting to combine columns',
        sortable: false,
        width: 150,
        valueGetter: (_params:GridValueGetterParams) => '${params.row.firstName || ""} ${params.row.lastName || ""}'
    }
];

const rows = [
    { id: 1, firstName: 'John', lastName: 'Doe', age: 30, fullname: 'John Doe' },
    { id: 2, firstName: 'Jane', lastName: 'Smith', age: 28, fullname: 'Jane Smith' },
    { id: 3, firstName: 'Michael', lastName: 'Johnson', age: 35, fullname: 'Michael Johnson' },
    { id: 4, firstName: 'Emily', lastName: 'Williams', age: 22, fullname: 'Emily Williams' },
    { id: 5, firstName: 'James', lastName: 'Brown', age: 40, fullname: 'James Brown' },
    { id: 6, firstName: 'Olivia', lastName: 'Taylor', age: 27, fullname: 'Olivia Taylor' },
    { id: 7, firstName: 'William', lastName: 'Lee', age: 33, fullname: 'William Lee' },
    { id: 8, firstName: 'Sophia', lastName: 'Martinez', age: 29, fullname: 'Sophia Martinez' },
    { id: 9, firstName: 'Alexander', lastName: 'Robinson', age: 31, fullname: 'Alexander Robinson' },
    { id: 10, firstName: 'Isabella', lastName: 'Hernandez', age: 26, fullname: 'Isabella Hernandez' }
  ];

  export const DataTable = () => {
    return (
        <Box sx={{height: 400, width: '100%'}}>
            <DataGrid
                rows={rows}
                columns={columns}
                initialState={{
                    pagination: {
                        paginationModel: {
                            pageSize: 5
                        }
                    }
                }}
                pageSizeOptions={[5]}
                checkboxSelection
                disableRowSelectionOnClick
                />
        </Box>
    )
}
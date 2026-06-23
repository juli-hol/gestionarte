import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface UIState {
  sidebarOpen: boolean
  globalLoading: boolean
}

const initialState: UIState = { sidebarOpen: true, globalLoading: false }

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    toggleSidebar(state) { state.sidebarOpen = !state.sidebarOpen },
    setLoading(state, action: PayloadAction<boolean>) { state.globalLoading = action.payload },
  },
})

export const { toggleSidebar, setLoading } = uiSlice.actions
export default uiSlice.reducer
